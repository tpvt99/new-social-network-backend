# response

from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import JsonResponse


# class-based view

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

# timezone

from django.utils import timezone
import time, datetime
import math
import json
import ast

# models

from page.models import City
from user.models import MyUser
from friend.models import Friend
from activity.models import Activity, ActivityParticipants
from act.models import Act as ActModel
from .models import ActivitiesPost, ActivitiesPostFriend
from status.models import Status
from noti.models import Notification, ActivitiesANotification

# python3 module

import ast
import time
from django.db.utils import IntegrityError
from django.db.models import Q

# Create your views here.

class Activities(View):
    template = 'activities/activities.html'
    def get(self, request):
        activity = Activity.objects.filter(Q(activity_activityparticipants_activity__person = request.user) & Q(activity_activityparticipants_activity__accepted = True)).order_by('-time_create')
        act = ActModel.objects.filter(user = request.user).order_by('-time_create')
        return render(request, self.template, {'acts':act,'activity':activity})

class FriendAjax(View):
    template = 'activities/friendajax.html'
    def get(self, request):
        key = request.GET.get('key')
        ex = request.GET.get('except')
        ex = ast.literal_eval(ex)
        if key:
            friends = Friend.objects.filter(user = request.user, friend__fullname__icontains = key).exclude(friend_id__in = ex)
        else:
            friends = None
        return render(request, self.template, {'friends':friends})

class Create(View):
    template = 'status/status.html'
    def post(self, request):
        data = request.POST
        try:
            x = int(request.POST.get('act_id'))
        except:
            return HttpResponse('error')
        activity = Activity.objects.get(pk__exact = x)
        if data.get('des').strip() != '':
            activitiespost =ActivitiesPost.objects.create(user= request.user, activity = activity, text = data.get('des'), privacy = request.POST.get('privacy'))
        else:
            return HttpResponse('error')
        if request.FILES.get('image'):
            activitiespost.image = request.FILES.get('image')
            activitiespost.save()
        fr_id = data.getlist('hiddenfr')
        if fr_id:
            for i in fr_id:
                t = MyUser.objects.get(pk__exact = int(i))
                ActivitiesPostFriend.objects.create(activitiespost =activitiespost , friend = t)
                noti = Notification.objects.create(user = t, noti_type = 'activities-a')
                ActivitiesANotification.objects.create(noti = noti, activity = activity, activitiespost = activitiespost)
        status = Status.objects.create(status_type = 'activitiespost', privacy =activitiespost.privacy,activitiespost =activitiespost , user = request.user)
        t=[]
        t.append(status)
        return render(request, self.template , {'status':t})
