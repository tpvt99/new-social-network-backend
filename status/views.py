# django response

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

#django setup

from django.db.utils import IntegrityError
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone

from a.settings import BASE_DIR

from .models import Status, StatusVote, StatusComment
from noti.models import Notification, StatusANotification, StatusBNotification, ActANotification, PostANotification
from user.models import MyUser, User
from act.models import Act, ActFriend
from friend.models import Friend
from post.models import Post as PostModel
from post.models import PostFriendTag
from plustag.models import PlustagLife
from plustag.models import Plustag
from plustag.models import PlustagVote as PlustagVoteModel
from plustag.models import plus_tag
from group.models import Group
from friend.models import Friend, FriendRelationship, FriendHeart
from activity.models import Activity
from event.models import Event
from contest.models import Contest

from security.response import set_response_header
from authentication.auth import check_authentication
from user.method import get_user

from .models import StatusReaction, StatusReactionVote

# pythone module

import random
import math
import re

# serialize

from status.serialize import status_serialize
from status.serialize import status_comment_serialize
from plustag.serialize import plustag_vote_serialize
from status.serialize import status_plustag_serialize
from status.reset_status_reaction import reset
from user.serialize import serialize_user_basic

# Create your views here.

class Fetch(View):
    def get(self, request):
        if check_authentication(request):
            user = get_user(request)
            # all or family or friends
            tab_section = request.GET.get('tab_section')
            try:
                currentIndex = int(request.GET.get('currentIndex'))
            except ValueError:
                currentIndex = 0
            fr = Friend.objects.filter(user = user).values_list('friend_id', flat=True)
            if tab_section == '':
                status = Status.objects.filter(Q(user = user) | Q(user_id__in = list(fr)), who_post = 'user', verb = 'post').order_by('-time_create')[currentIndex:currentIndex+10]
            elif tab_section == 'friend':
                status = Status.objects.filter(Q(user = user) | Q(user_id__in = list(fr)), who_post = 'user', verb = 'post').order_by('-time_create')[currentIndex:currentIndex+10]
            elif tab_section == 'sale':
                status = Status.objects.filter(Q(user = user) | Q(user_id__in = list(fr)), who_post = 'user', verb = 'sale').order_by('-time_create')[currentIndex:currentIndex+10]
            else:
                status = Status.objects.none()
            reset(status)
            data_serialize = status_serialize(status, user)
            data = {
                'data': data_serialize,
                'status_code': 'ok'
                }
            response = JsonResponse(data)
            set_response_header(response)
            return response

class FetchProfile(View):
    def get(self, request):
        try:
            currentIndex = int(request.GET.get('currentIndex'))
        except ValueError:
            currentIndex = 0
        try:
            user_profile_url = request.GET.get('profileUrl')
            user = User.objects.get(account__profilename = user_profile_url)
        except User.DoesNotExist:
            data = {
                'status_code': 'error'
                }
            response = JsonResponse(data)
            set_response_header(response)
            return response
        status = Status.objects.filter(user = user, verb = 'post').order_by('-time_create')[currentIndex:currentIndex+10]
        reset(status)
        data_serialize = status_serialize(status, user)
        data = {
            'data': data_serialize,
            'status_code': 'ok'
            }
        response = JsonResponse(data)
        set_response_header(response)
        return response


class Vote(View):
    def post(self, request):
        if check_authentication(request):
            user = get_user(request)
            try:
                reactionPk = int(request.POST.get('reaction'))
                reaction_type = request.POST.get('type')
            except ValueError:
                return JsonResponse({'status_type':'ok'})
            status_reaction = StatusReaction.objects.get(pk = reactionPk, reactionType = reaction_type)
            status = status_reaction.status
            try:
                #vote = StatusVote.objects.create(user = user, status = status)
                #status.vote += 1
                #status.save()
                #vote.been_vote = True
                #vote.save()
                #if status.user and user != status.user:
                #    noti = Notification.objects.create(user = status.user, noti_type = 'status-a')
                #    StatusANotification.objects.create(noti = noti, status = status, who_vote = user)

                reaction_vote = StatusReactionVote.objects.create(statusreaction = status_reaction, user = user)
                # specific reaction of status
                status_reaction.vote += 1
                status_reaction.save()
                reaction_vote.been_vote = True
                reaction_vote.save()
                # the whole votes for all reactions
                status.vote += 1
                status.save()
                if status.user and user != status.user:
                    noti = Notification.objects.create(user = status.user, noti_type = 'status-a')
                    StatusANotification.objects.create(noti = noti, status = status, user = user)
            except IntegrityError:
                #vote = StatusVote.objects.get(user = user, status = status)
                #if vote.been_vote == True:
                #    status.vote -= 1
                #    status.save()
                #    vote.been_vote = False
                #    vote.save()
                #else:
                #    status.vote += 1
                #    status.save()
                #    vote.been_vote = True
                #    vote.save()
                reaction_vote = StatusReactionVote.objects.get(statusreaction = status_reaction, user = user)
                if reaction_vote.been_vote == True:
                    reaction_vote.been_vote = False
                    reaction_vote.save()
                    status_reaction.vote -= 1
                    status_reaction.save()
                    status.vote -= 1
                    status.save()
                else:
                    reaction_vote.been_vote = True
                    reaction_vote.save()
                    status_reaction.vote += 1
                    status_reaction.save()
                    status.vote += 1
                    status.save()
            heart = 0
            if status.user:
                try:
                    friend = status.user
                    x = Friend.objects.get(user = user, friend = friend)
                    try:
                        t = FriendRelationship.objects.get(user = user, friend = x)
                    except FriendRelationship.DoesNotExist:
                         t = FriendRelationship.objects.create(user = user, friend = x)
                    finally:
                        try:
                            a = FriendHeart.objects.get(user = user, friend = friend, friendrelationship = t, source = 'status',reason = 'like',status = status)
                        except FriendHeart.DoesNotExist:
                            a = FriendHeart.objects.create(user = user, friend = friend, friendrelationship = t, source = 'status',reason = 'like',status = status)
                        finally:
                            if reaction_vote.been_vote == True:
                                a.heart = 1
                                t.friend_heart += a.heart
                            else:
                                t.friend_heart -= a.heart
                                a.heart = 0
                            a.save()
                            t.save()
                            zz = FriendHeart.objects.filter(user = user, friend = friend, friendrelationship = t, status = status)
                            for i in zz:
                                heart += i.heart
                except Friend.DoesNotExist:
                    pass
            response = JsonResponse({
                'been_vote': reaction_vote.been_vote,
                'user': {'user': serialize_user_basic(user)},
                'status_type':'ok'
                })
            set_response_header(response)
            return response


class Comment(View):
    def define_plustag(self, status, user_send_plus, comment):
        re_exp = re.compile(r'^\+[\w]+| \+[\w]+')
        re_result = list(set(re_exp.findall(comment)))
        for i in re_result:
            try:
                if status.user:
                    Plustag.objects.create(user_receive_plus = status.user, user_send_plus = user_send_plus, status = status, plustag_name = i.strip(), votes = 1)
                else:
                    Plustag.objects.create(user_send_plus = user_send_plus, status = status, plustag_name = i.strip(), votes = 1)
            except IntegrityError:
                x = Plustag.objects.get(status = status, plustag_name = i.strip())
                if x.user_send_plus != user_send_plus:
                    try:
                        pv = PlustagVoteModel.objects.create(plustag = x, user_vote = user_send_plus, been_vote = True)
                        x.votes += 1
                        x.save()
                    except IntegrityError:
                        pass

    
    def get(self, request):
        feedPk = request.GET.get('feedPk')
        totalFetch = int(request.GET.get('totalFetch')) if request.GET.get('totalFetch') else 10
        currentIndex = int(request.GET.get('currentIndex'))
        status = Status.objects.get(pk = int(feedPk))
        comments = status_comment_serialize(status, totalFetch, currentIndex)
        response = JsonResponse({'comments': comments,'status_type':'ok'})
        set_response_header(response)
        return response


    def post(self, request):
        if check_authentication(request, True):
            user = get_user(request)
            data = request.POST
            try:
                status = Status.objects.get(pk__exact = int(request.POST.get('feed_pk')))
            except Status.DoesNotExist:
                return JsonResponse({'status_type':'error'})
            sc = StatusComment.objects.create(user = user, status = status, comment = request.POST.get('text'))
            self.define_plustag(status, user, request.POST.get('text'))
            if status.user and user != status.user:
                noti = Notification.objects.create(user = status.user, noti_type = 'status-b')
                StatusBNotification.objects.create(noti = noti, status = status, statuscomment = sc)
            # friendship

            #if status.user:
            #    try:
            #        friend = status.user
            #        x = Friend.objects.get(user = user, friend = friend)
            #        try:
            #            t = FriendRelationship.objects.get(user = user, friend = x)
            #        except FriendRelationship.DoesNotExist:
            #             t = FriendRelationship.objects.create(user = user, friend = x)
            #        finally:
            #            try:
            #                a = FriendHeart.objects.get(user = user, friend = friend, friendrelationship = t, source = 'status',reason = 'comment',status = status)
            #            except FriendHeart.DoesNotExist:
            #                a = FriendHeart.objects.create(user = user, friend = friend, friendrelationship = t, source = 'status',reason = 'comment',status = status)
            #                a.heart = random.randint(1,2)
            #                t.friend_heart += a.heart
            #                a.save()
            #                t.save()
            #    except Friend.DoesNotExist:
            #        pass
            comment = status_comment_serialize(status, 1)
            response = JsonResponse({'comments': comment,'plustags': status_plustag_serialize(status), 'status_type':'ok'})
            set_response_header(response)
            return response


class PlustagVote(View):
    def post(self, request):
        if check_authentication(request):
            user = get_user(request)
            try:
                pk = int(request.POST.get('plustagPk'))
            except:
                response = JsonResponse({'status_code': 'error'})
                set_response_header(response)
                return response
            plustag = Plustag.objects.get(pk = pk)
            if plustag.user_send_plus == user:
                data = {
                    'data': plustag_vote_serialize(plustag),
                    'status_code': 'ok'
                    }
                response = JsonResponse(data)
                set_response_header(response)
                return response
            else:
                try:
                    pv = PlustagVoteModel.objects.create(plustag = plustag, user_vote = user, been_vote = True)
                    plustag.votes += 1
                    plustag.save()
                    data = {
                        'data': plustag_vote_serialize(plustag),
                        'status_code': 'ok'
                        }
                    response = JsonResponse(data)
                    set_response_header(response)
                    return response
                except IntegrityError:
                    pv = PlustagVoteModel.objects.get(plustag = plustag, user_vote = user)
                    if pv.been_vote == True:
                        pv.been_vote = False
                        pv.save()
                        plustag.votes -= 1
                        plustag.save()
                    else:
                        pv.been_vote = True
                        pv.save()
                        plustag.votes += 1
                        plustag.save()
                    data = {
                    'data': plustag_vote_serialize(plustag),
                    'status_code': 'ok'
                    }
                    response = JsonResponse(data)
                    set_response_header(response)
                    return response


class PlustagDelete(View):
    def post(self, request):
        if check_authentication(request):
            user = get_user(request)
            try:
                pk = int(request.POST.get('plustagPk'))
            except:
                response = JsonResponse({'status_code': 'error'})
                set_response_header(response)
                return response
            plustag = Plustag.objects.get(pk = pk)
            status = plustag.status
            if status.user == user:
                plustag.delete()
                response = JsonResponse({'status_code': 'ok'})
                set_response_header(response)
                return response
            else:
                response = JsonResponse({'status_code': 'error'})
                set_response_header(response)
                return response
