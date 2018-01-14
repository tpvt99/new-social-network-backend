from django.shortcuts import render
from django.views.generic import View
from user.models import MyUser
from user.models import User
from django.utils import timezone
import time

from django.http import JsonResponse, HttpResponse
import json
from datetime import timedelta

from django.core.urlresolvers import reverse
from friend.models import Friend
from django.db.models import Q

from .models import Message
from .models import MessageUser as MessageFrame
from .models import MessageUserInfo
from .models import MessageReadInfo

# authentication and user
from authentication.auth import check_authentication 
from user.method import get_user
from .serialize import friend_serialize
from security.response import set_response_header
from security.response import response_error
from user.serialize import serialize_user_basic
from message.serialize import message_serialize
from .serialize import pollmessage_serialize

# Create your views here.

class ChatOnline(View):
    def get(self, request):
        if check_authentication(request):
            user = get_user(request)
            past_5_days = timezone.now() - timedelta(days = 5)
            #friend = Friend.objects.filter(user = user, friend__onlinetime__time__gte = past_5_days)
            friend = Friend.objects.filter(user = user)
            data = {
            'friends': friend_serialize(friend),
            'status_code': 'ok'
            }
            response = JsonResponse(data)
            set_response_header(response)
            return response


class ChatFrameInformation(View):
    def get(self, request):
        if check_authentication(request):
            user_request = get_user(request)
            try:
                total = int(request.GET.get('total'))
            except:
                response_error()
            target = request.GET.get('target')
            user_receive_id = request.GET.getlist('listId[]')
            #now it is just 1 item in user_receive_id
            user_receive_id = user_receive_id[0]
            try:
                user_receive = User.objects.get(user_id = user_receive_id)
            except User.DoesNotExist:
                response_error()
            if total == 2 and target == 'user':
                m = MessageFrame.objects.filter(message_type = 'user').filter(users = user_request).filter(users = user_receive)
                if len(m) == 1 and len(m[0].users.all()) == 2:
                    data = {
                    'frame_id': m[0].id,
                    'status_code': 'ok',
                    'users': [serialize_user_basic(user_request), serialize_user_basic(user_receive)]
                    }
                elif len(m) == 0:
                    m = MessageFrame.objects.create(message_type = 'user')
                    m.users.add(user_request)
                    m.users.add(user_receive)
                    m.save()
                    data = {
                    'frame_id': m.id,
                    'status_code': 'ok',
                    'users': [serialize_user_basic(user_request), serialize_user_basic(user_receive)]
                    }
                else:
                    data = {
                    'status_code': 'error'
                    }
            else:
                data = {
                'status_code': 'error'
                }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'text/javascript')
            set_response_header(response)
            return response


class SendMessage(View):
    def post(self, request):
        if check_authentication(request):
            user_request = get_user(request)
            text = request.POST.get('text')
            frame_id = request.POST.get('frameId')
            try:
                frame_id = int(frame_id)
            except:
                response_error()
            chat_frame = MessageFrame.objects.get(pk = frame_id)
            if text:
                m = Message.objects.create(user_send = user_request, chat_frame = chat_frame, text = text)
                # create or get a messageFrameInfo to detect user read or not read
                users_of_chat_frame = chat_frame.users.all()
                for user in users_of_chat_frame:
                    try:
                        a = MessageUserInfo.objects.get(frame = chat_frame, user = user)
                    except MessageUserInfo.DoesNotExist:
                        a = MessageUserInfo.objects.create(frame = chat_frame, user = user)
                    if user != user_request:
                        a.read = False
                        a.fetch = False
                        a.save()
                        # here to create messagereadInfo for each message
                        mri = MessageReadInfo.objects.create(user = user, message = m, read = False, fetch = False)
            data = {
            'status_code': 'ok',
            'mess': message_serialize(m)
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8')
            set_response_header(response)
            return response


class GetMessage(View):
    def get(self, request):
        if check_authentication(request):
            user = get_user(request)
            c_index = int(request.GET.get('cIndex')) if request.GET.get('cIndex') else 0
            try:
                frame_id = request.GET.get('frameId')
                frame_id = int(frame_id)
            except:
                response_error()
            chat_frame = MessageFrame.objects.get(pk = frame_id)
            if user in chat_frame.users.all() and c_index != -1:
                m = Message.objects.filter(chat_frame = chat_frame).order_by('-create_time')[c_index:c_index+10]
            elif user in chat_frame.users.all():
                m = Message.objects.filter(chat_frame = chat_frame, message_messagereadinfo_message__fetch = False)
                # here to reset the fetch in messageReadInfo
            mess = message_serialize(m)
            # line next and for loop to reset the message read and fetch
            mri = MessageReadInfo.objects.filter(user = user).filter(message_id__in = list(m.values_list('id', flat = True)))
            for i in mri:
                i.fetch = True
                i.save()
            data = {
            'status_code': 'ok',
            'mess': mess
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8')
            set_response_header(response)
            return response

class PollMessage(View):
    def get(self, request):
        if check_authentication(request):
            user = get_user(request)
            timeout = time.time() + 45 # 3 seconds
            while True:
                time.sleep(2)
                if time.time() > timeout:
                    break
                m = MessageUserInfo.objects.filter(user = user, fetch = False)
                if len(m) > 0:
                    data = {
                    'data': pollmessage_serialize(m),
                    'status_code': 'ok',
                    'on': True
                    }
                    response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                    set_response_header(response)
                    return response
            data = {
            'status_code': 'ok',
            'on': False
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
            set_response_header(response)
            return response
        data = {
        'status_code': 'error'
        }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
        set_response_header(response)
        return response
