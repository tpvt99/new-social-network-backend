from django.shortcuts import render
from django.views.generic import View
from django.db.utils import IntegrityError
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
# model
from .models import OnlineTime
from friend.models import Friend

from user.method import get_user
from authentication.auth import check_authentication
from security.response import set_response_header
from message.serialize import on_friend_serialize
from user.serialize import serialize_user_basic

import json

from .models import FollowTimeline

# Create your views here.

class Online(View):
    def post(self, request):
        if check_authentication(request):
            user = get_user(request)
            try:
                a = OnlineTime.objects.create(user = user)
            except IntegrityError:
                a = OnlineTime.objects.get(user = user)
                a.time = timezone.now()
                a.save()
                data = {
                    'status_code': 'ok',
                }
                response = HttpResponse('while(1);' + json.dumps(data), content_type = 'text/javascript')
                set_response_header(response)
                return response
        else:
            response = JsonResponse({'status_code': 'error'})
            set_response_header(response)
            return response

class TabFollowers(View):
    def post(self, request):
        tab_id = request.GET.get('tab_id')

        tab_name = request.POST.get('tab_name')
        
        # action type is delete user or add user
        action_type = request.POST.get('action_type')

        if check_authentication(request):
            user = get_user(request)
            if action_type == 'create_tab':
                try:
                    a = FollowTimeline.objects.get(name = tab_name, user = user)
                    data = {
                    'status_code': 'error'
                    }
                except FollowTimeline.DoesNotExist:
                    a = FollowTimeline.objects.create(name = tab_name, user = user)
                    data = {
                    'status_code': 'ok'
                    }
                response = JsonResponse(data)
                set_response_header(response)
                return response
                    

    def get(self, request):
        # tab id of each tab. If this is empty, it means that tab has not created. This is required
        tab_id = request.GET.get('tab_id')

        # tab name of each tab. This is optional because searching not based on name but based on id. When tab_id is empty, this must be not empty. Such as 'family' because it has created on client but not on the server so it has name but not has id yet
        tab_name = request.GET.get('tab_name')

        # type of GET request: 'fetch_user' is fetching all User in this tab and 'filter_user' is filtering User when user type name in input
        action_type = request.GET.get('action_type')

        # input_name is text user type in input to filter user has not been in this tab
        input_name = request.GET.get('input_name')

        # friend Ids is the ID has been typed in input field. Those will be filtered out for the results.
        friendIds = request.GET.getlist('friend_ids')

        # check authentication and get user
        if check_authentication(request):
            user = get_user(request)
            if action_type == 'fetch_user':
                if tab_id:
                    try:
                        TabFollower = FollowTimeline.objects.get(follow_id = tab_id, user = user)
                        users = TabFollower.members.all()
                        data_se =[]
                        for i in users:
                            data_se.append(serialize_user_basic(i))
                        data = {
                        'status_code': 'ok',
                        'data': data_se
                        }
                    except FollowTimeline.DoesNotExist:
                        data = {
                        'status_code': 'error'
                        }
                elif tab_name:
                    try:
                        TabFollower = FollowTimeline.objects.get(name = tab_name, user = user)
                        users = TabFollower.members.all()
                        data_se =[]
                        for i in users:
                            data_se.append(serialize_user_basic(i))
                        data = {
                        'status_code': 'ok',
                        'data': data_se
                        }
                    except FollowTimeline.DoesNotExist:
                        data = {
                        'status_code': 'error'
                        }
                else:
                    data = {
                    'status_code': 'ok'
                    }
                response = JsonResponse(data)
                set_response_header(response)
                return response
            elif action_type == 'filter_user':
                if tab_id:
                    try:
                        TabFollower = FollowTimeline.objects.get(follow_id = tab_id, user = user)
                        users_id_in_tab_followers = TabFollower.members.all().values_list('id', flat = True)
                        friends = Friend.objects.filter(friend__fullname__icontains = input_name, user = user).exclude(friend__user_id__in = users_id_in_tab_followers).exclude(friend__user_id__in = friendIds)
                        data_se = []
                        for i in friends:
                            data_se.append(serialize_user_basic(i.friend))
                        data = {
                        'status_code': 'ok',
                        'data': data_se
                        }
                    except FollowTimeline.DoesNotExist:
                        data = {
                        'status_code': 'error'
                        }
                elif tab_name:
                    try:
                        TabFollower = FollowTimeline.objects.get(name = tab_name, user = user)
                        users_id_in_tab_followers = TabFollower.members.all().values_list('id', flat = True)
                        friends = Friend.objects.filter(friend__fullname__icontains = input_name, user = user).exclude(friend__user_id__in = users_id_in_tab_followers).exclude(friend__user_id__in = friendIds)
                        data_se =[]
                        for i in friends:
                            data_se.append(serialize_user_basic(i.friend))
                        data = {
                        'status_code': 'ok',
                        'data': data_se
                        }
                    except FollowTimeline.DoesNotExist:
                        data = {
                        'status_code': 'error'
                        }
                else:
                    data = {
                    'status_code': 'ok'
                    }
                response = JsonResponse(data)
                set_response_header(response)
                return response
            else:
                data = {
                'status_code': 'error'
                }
                response = JsonResponse(data)
                set_response_header(response)
                return response
