from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from files.models import Image
from django.db.utils import IntegrityError
import json
import time

from django.views.generic import View
from security.response import set_response_header
from security.response import response_error
from user.method import get_user
from .method import get_network_account
from .serialize import network_goal_serialize 
from .serialize import network_serialize
from .serialize import network_chat_frame_serialize
from .serialize import network_message_serialize
from .serialize import pull_message_serialize
from .serialize import network_account_serialize
from .serialize import topic_serialize
from .serialize import network_chatroom_serialize

from authentication.auth import check_authentication


from .models import NetworkAccount
from .models import NetworkGoal
from .models import NetworkChatFrame
from .models import NetworkChatUser
from .models import NetworkMessage
from .models import NetworkMessageInfo
from .models import NetworkChatroomTopic
from .models import NetworkChatroom
from .models import NetworkChatroomUser

# Create your views here.

class Register(View):
    def post(self, request):
        if check_authentication(request):
            user = get_user(request)
            post_data = request.POST
            fullname = post_data.get('fullname')
            born_year = post_data.get('bornYear')
            image_id = post_data.get('imageId')
            country_code = post_data.get('countryCode')
            sex = post_data.get('sex')
            if user and fullname and born_year and image_id and sex and country_code:
                image = Image.objects.get(pk = image_id)
                try:
                    NetworkAccount.objects.create(user = user, fullname = fullname, birthYear = born_year, nationality = country_code, sex = sex, profile_picture = image)
                except IntegrityError:
                    data = {
                        'status_code': 'error'
                    }
                    response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                    return response
                data = {
                    'status_code': 'ok'
                }
                response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                return response
            data = {
                'status_code': 'error'
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
            set_response_header(response)
            return response

class GetProfileInfo(View):
    def get(self, request):
        network_id = request.GET.get('network_id')
        try:
            user = NetworkAccount.objects.get(network_id = network_id)
        except NetworkAccount.DoesNotExist:
            data = {
            'status_code': 'error'
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/json')
            set_response_header(response)
            return response
        data = {
        'status_code': 'ok',
        'user': network_account_serialize(user),
        }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/json')
        set_response_header(response)
        return response

class Goal(View):
    def get(self, request):
        network_account = get_network_account(request)
        if network_account:
            goals = NetworkGoal.objects.filter(user_account = network_account)
            goal_serialize = network_goal_serialize(goals)
            data = {
                'status_code': 'ok',
                'goal': goal_serialize
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = "application/x-javascript; charset=utf-8")
            set_response_header(response)
            return response

    def post(self, request):
        data = request.POST
        nu = request.COOKIES.get('nu')
        if nu:
            try:
                network_account = NetworkAccount.objects.get(network_id = nu)
            except NetworkAccount.DoesNotExist:
                data = {
                'status_code': 'error'
                }
                response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                return response
            # post_type is delete or create or modify
            post_type = request.POST.get('type')
            introduction = request.POST.get('introduction')
            goal = request.POST.get('goal')
            select_goal = request.POST.get('select_goal')
            if post_type == 'create':
                try:
                    mmm = NetworkGoal.objects.get(user_account = network_account, gola = goal, select_goal = select_goal)
                    mmm.delete()
                except:
                    pass
                a = NetworkGoal.objects.create(user_account = network_account, goal = goal, select_goal = select_goal, introduction = introduction)
                data = {
                'status_code': 'ok'
                }
                response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                return response
        else:
            data = {
            'status_code': 'error'
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
            return response

class GetNetwork(View):
    def get_goal(offset):
        goal_list = ['sport', 'language']

    def get(self, request):
        # this is section which is all or sport or language to filter
        tab_section = request.GET.get('tab_section')
        # the total number of current to fetch continuos
        number_offset = request.GET.get('number_offset')
        if tab_section and number_offset:
            try:
                number_offset = int(number_offset)
            except:
                number_offset = 0
            if tab_section == 'all':
                t = NetworkGoal.objects.filter(goal = 'sport')
                a = NetworkGoal.objects.filter(goal = 'language')
                data = []
                data.append(network_serialize(t, 'sport'))
                data.append(network_serialize(a, 'language'))
                data_response = {
                'status_code': 'ok',
                'data': data
                }
                response = JsonResponse(data_response)
                set_response_header(response)
                return response
        data_response = {
        'status_code': 'error',
        }
        response = JsonResponse(data_response)
        set_response_header(response)
        return response

    # this view is used to get the people chatted with you to render in the top of the page
class GetNetworkPeople(View):
    def get(self, request):
        nu = request.COOKIES.get('nu')
        user = NetworkAccount.objects.get(network_id = nu)
        a = NetworkChatFrame.objects.filter(users = user, frame_type = 'goal')
        all_frames = []
        for i in a:
            all_frames.append(network_chat_frame_serialize(i))
        data_response = {
        'status_code': 'ok',
        'all_frames': all_frames
        }
        response = HttpResponse('while(1);'+ json.dumps(data_response), content_type = 'application/x-javascript; charset=utf-8')
        set_response_header(response)
        return response

# this class is getting messages from a frame

class GetNetworkMessage(View):
    """ Return messages of frame
    frame_id is id of the frame
    current_index is the number of current messages has been fetched out
    nu is the network_id stored in cookie of browser"""
    def get(self, request):
        frame_id = request.GET.get('frameId')
        current_index = request.GET.get('cIndex') if request.GET.get('cIndex') else 0
        nu = request.COOKIES.get('nu')
        if frame_id and current_index and nu:
            try:
                frame_id = int(frame_id)
                current_index = int(current_index)
            except:
                data = {
                    'status_code': 'error'
                }
                response = JsonResponse(data, content_type = "application/json")
                set_response_header(response)
                return response
            network_frame = NetworkChatFrame.objects.get(id = frame_id)
            user_send = NetworkAccount.objects.get(network_id = nu)
            if user_send in network_frame.users.all() and current_index != -1:
                m = NetworkMessage.objects.filter(chat_frame = network_frame).order_by('-create_time')[current_index:current_index+10]
            elif user_send in network_frame.users.all() and current_index == -1:
                m = NetworkMessage.objects.filter(chat_frame = network_frame, network_networkmessageinfo_network_message__fetch = False)
            # line next and for loop to reset the message read and fetch
            m_serialize = network_message_serialize(m)
            nmf = NetworkMessageInfo.objects.filter(user = user_send).filter(network_message_id__in = list(m.values_list('id', flat=True)))
            for i in nmf:
                i.fetch = True
                i.read = True
                i.save()
            data = {
            'status_code': 'ok',
            'messages': m_serialize
            }
            response = JsonResponse(data, content_type = "application/json")
            set_response_header(response)
            return response


class GetNetworkFrame(View):
    def get(self, request):
        data = request.GET
        user_request_id = request.COOKIES.get('nu')
        user_receive_id = request.GET.getlist('users[]')
        total_people = request.GET.get('total_people')
        frame_id = request.GET.get('frameId')
        if frame_id:
            user_request = NetworkAccount.objects.get(network_id = user_request_id)
            network_chat_frame = NetworkChatFrame.objects.get(id = int(frame_id))
            if user_request in network_chat_frame.users.all():
                data_response = network_chat_frame_serialize(network_chat_frame)
                data = {
                'status_code': 'ok',
                'data': data_response
                }
                response = HttpResponse('while(1);'+ json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                set_response_header(response)
                return response
        if user_request_id and user_receive_id and total_people and user_request_id not in user_receive_id:
            try:
                user_request = NetworkAccount.objects.get(network_id = user_request_id)
                network_chat_frame = NetworkChatFrame.objects.filter(users = user_request)
                for i in range(0, int(total_people) - 1):
                    user_receive = NetworkAccount.objects.get(network_id = user_receive_id[i])
                    network_chat_frame = network_chat_frame.filter(users = user_receive)
            except:
                data = {
                    'status_code': 'error'
                }
                response = HttpResponse('while(1);'+ json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                set_response_header(response)
                return response
            frame_exist = False
            for i in network_chat_frame:
                if int(total_people) == len(i.users.all()):
                    data_response = network_chat_frame_serialize(i)
                    frame_exist = True
                    break
            if not frame_exist:
                network_chat_frame = NetworkChatFrame.objects.create()
                network_chat_frame.users.add(user_request)
                NetworkChatUser.objects.create(frame = network_chat_frame, user = user_request)
                for i in range(0, int(total_people) - 1):
                    user_receive = NetworkAccount.objects.get(network_id = user_receive_id[i])
                    network_chat_frame.users.add(user_receive)
                    NetworkChatUser.objects.create(frame = network_chat_frame, user = user_receive)
                data_response = network_chat_frame_serialize(network_chat_frame)
            data = {
            'status_code': 'ok',
            'data': data_response
            }
        else:
            data = {
            'status_code': 'error'
            }
        response = HttpResponse('while(1);'+ json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
        set_response_header(response)
        return response

class SendNetworkMessage(View):
    def post(self, request):
        nu = request.COOKIES.get('nu')
        text = request.POST.get('text')
        frame_id = request.POST.get('frameId')
        try:
            user = NetworkAccount.objects.get(network_id = nu)
            frame = NetworkChatFrame.objects.get(id = int(frame_id))
        except:
            data = {
            'status_code': 'error'
            }
            response = HttpResponse('while(1);'+ json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
            set_response_header(response)
            return response
        if text and len(text) != 0:
            m = NetworkMessage.objects.create(user_send = user, chat_frame = frame, text = text)
            users_of_frame = frame.users.all()
            for i in users_of_frame:
                if i != user:
                    a = NetworkChatUser.objects.get(user = i, frame = frame)
                    a.read = False
                    a.fetch = False
                    a.save()
                    NetworkMessageInfo.objects.create(user = i, network_message = m, read = False, fetch = False)
        data = {
        'status_code': 'ok',
        'mess': network_message_serialize(m)
        }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8')
        set_response_header(response)
        return response

class PullNetworkMessage(View):
    def get(self, request):
        user = NetworkAccount.objects.get(network_id = request.COOKIES.get('nu'))
        timeout = time.time() + 50 # 10 seconds
        while True:
            time.sleep(2)
            if time.time() > timeout:
                break
            m = NetworkChatUser.objects.filter(user = user, fetch = False)
            for i in m:
                i.fetch = True
                i.read = True
                i.save()
            if len(m) > 0:
                data = {
                'data': pull_message_serialize(m),
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

class SearchTopicChatroom(View):
    # this get request returns all topics when search with a key or all rooms of a specific topic
    def get(self, request):
        action = request.GET.get('action')
        # return all topics that match key search
        if action == 'topic':
            key = request.GET.get('search')
            result = NetworkChatroomTopic.objects.filter(name__icontains = key)[0:10]
            data = {
            'status_code': 'ok',
            'data': topic_serialize(result)
            }
        # return all rooms of this topic
        elif action == 'topic_room':
            topic_url = request.GET.get('topic_url')
            try:
                topic = NetworkChatroomTopic.objects.get(url = topic_url)
                chatroom = NetworkChatroom.objects.filter(tag_topic = topic)
                data = {
                'status_code': 'ok',
                'topic': topic_serialize(topic),
                'data': network_chatroom_serialize(chatroom)
                }
            except:
                data = {
                'status_code': 'error'
                }
        else:
            data = {
            'status_code': 'error'
            }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
        set_response_header(response)
        return response

class TopicChatroom(View):
    def post(self, request):
        nu = request.COOKIES.get('nu')
        network_account = NetworkAccount.objects.get(network_id = nu)
        action = request.POST.get('action')
        if action == 'create_topic':
            topic_name = request.POST.get('topic')
            topic_description = request.POST.get('topic_description')
            if topic_name != '' and topic_description != '':
                topic_url = '-'.join(topic_name.split())
                try:
                    a = NetworkChatroomTopic.objects.get(url__iexact = topic_url)
                    data = {
                    'status_code': 'duplicate'
                    }
                    response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
                    set_response_header(response)
                    return response
                except NetworkChatroomTopic.DoesNotExist:
                    a = NetworkChatroomTopic.objects.create(name = topic_name, description = topic_description, user = network_account, url = topic_url)
                    data = {
                    'status_code': 'ok',
                    'topic_name': a.url
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

class ChatroomSettings(View):
    def get(self, request):
        nu = request.COOKIES.get('nu')
        action = request.GET.get('action')
        if action == 'get_room_data':
            room_id = request.GET.get('room_id')
            network_account = NetworkAccount.objects.get(network_id = nu)
            # this is all chatrooms of the user is chatting and the owner too
            if room_id == 'all':
                network_chatroom = NetworkChatroom.objects.filter(owner = network_account)
                data = {
                'status_code': 'ok',
                'data': network_chatroom_serialize(network_chatroom),
                'action': 'all'
                }
            else:
                try:
                    room_id = int(room_id)
                    try:
                        # currently it is filter for the owner of chatroom to access it
                        network_chatroom = NetworkChatroom.objects.get(id = room_id, owner = network_account)
                        data = {
                        'status_code': 'ok',
                        'data': network_chatroom_serialize(network_chatroom),
                        'action': 'one'
                        }
                    # this except is when no room is found
                    except NetworkChatroom.DoesNotExist:
                        data = {
                        'status_code': 'error',
                        'action': 'error'
                        }
                # this except is when the room_id is not a number
                except:
                    data = {
                    'status_code': 'error',
                    'action': 'error'
                    }
        else:
            data = {
            'status_code': 'error',
            'action': 'error'
            }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8')
        return response

    def post(self, request):
        nu = request.COOKIES.get('nu')
        network_account = NetworkAccount.objects.get(network_id = nu)
        action = request.POST.get('action')
        # creating room
        if action == 'create_room':
            room_name = request.POST.get('room_name')
            room_description = request.POST.get('room_des')
            tag_topic_id = request.POST.getlist('tag_topic_id')
            a = NetworkChatroom.objects.create(name = room_name, description = room_description, owner = network_account)
            # add topic
            for i in tag_topic_id:
                topic = NetworkChatroomTopic.objects.get(id = int(i))
                a.tag_topic.add(topic)
            
            # add frame
            frame = NetworkChatFrame.objects.create(frame_type = 'room')
            frame.users.add(network_account)
            NetworkChatUser.objects.create(frame = frame, user = network_account)
            a.chat_frame = frame
            a.save()
            # add info for each user - owner in this case
            NetworkChatroomUser.objects.create(chatroom = a, user = network_account, allow_join = True)
            data = {
                'status_code': 'ok',
                'data': {
                    'room_id': a.id
                }
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8');
            set_response_header(response)
            return response
        elif action == 'join_room':
            room_id = request.POST.get('room_id')
            room_id = int(room_id)
            chatroom = NetworkChatroom.objects.get(pk = room_id)
            try:
                NetworkChatroomUser.objects.get(chatroom = chatroom, user = network_account)
                data = {
                'status_code': 'error'
                }
            except NetworkChatroomUser.DoesNotExist:
                NetworkChatroomUser.objects.create(chatroom = chatroom ,user = network_account, allow_join = False)
                data = {
                'status_code': 'ok',
                }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8');
            set_response_header(response)
            return response
        # this is method for canceling request of joining room from user who request not from owner
        elif action == 'cancel_room':
            room_id = request.POST.get('room_id')
            room_id = int(room_id)
            chatroom = NetworkChatroom.objects.get(pk = room_id)
            try:
                a = NetworkChatroomUser.objects.get(chatroom = chatroom, user = network_account, allow_join = False)
                a.delete()
                data = {'status_code': 'ok'}
            except NetworkChatroomUser.DoesNotExist:
                data = {'status_code': 'ok'}
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8');
            set_response_header(response)
            return response
        elif action == 'accept_room':
            room_id = request.POST.get('room_id')
            room_id = int(room_id)
            chatroom = NetworkChatroom.objects.get(pk = room_id)
            accept_id = request.POST.get('accept_id')
            network_accept_account = NetworkAccount.objects.get(network_id = accept_id)
            try:
                if network_account != chatroom.owner:
                    raise ValueError('Not the owner')
                a = NetworkChatroomUser.objects.get(chatroom = chatroom, user = network_accept_account, allow_join = False)
                a.allow_join = True
                a.save()
                data = {'status_code': 'ok'}
            except NetworkChatroomUser.DoesNotExist:
                data = {'status_code': 'error'}
            except ValueError:
                data = {'status_code': 'error'}
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8');
            set_response_header(response)
            return response
        elif action == 'owner_cancel_room':
            room_id = request.POST.get('room_id')
            room_id = int(room_id)
            chatroom = NetworkChatroom.objects.get(pk = room_id)
            accept_id = request.POST.get('accept_id')
            network_accept_account = NetworkAccount.objects.get(network_id = accept_id)
            try:
                if network_account != chatroom.owner:
                    raise ValueError('Not the owner')
                a = NetworkChatroomUser.objects.get(chatroom = chatroom, user = network_accept_account, allow_join = False)
                a.delete()
                data = {'status_code': 'ok'}
            except NetworkChatroomUser.DoesNotExist:
                data = {'status_code': 'error'}
            except ValueError:
                data = {'status_code': 'error'}
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript;charset=utf-8');
            set_response_header(response)
            return response
