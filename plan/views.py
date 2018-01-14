# response

from django.shortcuts import render
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponseBadRequest
from django.http import JsonResponse

# generic view

from django.db.utils import IntegrityError
from django.views.generic import View
from django.utils import timezone

# python libarary

import ast
import json

# models

from .models import Plan, PlanParticipants, ParticipantMoreInfo
from user.models import MyUser
from page.models import City

# Create your views here.

class Helper(View):
    def add_participants(self, plan, friends, user):
        fr_list = friends.split(',')
        planparticipants = PlanParticipants.objects.create(plan = plan)
        if fr_list[0] and fr_list:
            for fr in fr_list:
               person = MyUser.objects.get(pk__exact = int(fr)) 
               info = ParticipantMoreInfo.objects.create(person = person, planparticipants = planparticipants, plan = plan)
               info.owner_invited = True
               info.save()
        info = ParticipantMoreInfo.objects.create(person = user, planparticipants = planparticipants, plan = plan)
        info.is_join = True
        info.save()

    def add_place(self, plan, city, address):
        if city != 'undefined' and city:
            city_obj = City.objects.get(city_code = city)
            plan.city = city_obj
            plan.city_code = city
            plan.save()
        if address != 'undefined' and address:
            plan.address = address
            plan.save()

    def add_timezone(self, plan, timezone):
        plan.timezone = int(timezone)
        plan.save()

    def add_time(self, plan, year, month, day, hour , minute):
        time = timezone.now()
        time = time.replace(month=1, day = 1, hour = 0, minute = 0, microsecond = 0)
        if year:
            time = time.replace(year = int(year))
            plan.time_year = True
            plan.save()
        if month:
            time = time.replace(month = int(month))
            plan.time_month = True
            plan.save()
        if day:
            time = time.replace(day = int(day))
            plan.time_day = True
            plan.save()
        if hour:
            time = time.replace(hour = int(hour))
            plan.time_hour = True
            plan.save()
        if minute:
            time = time.replace(minute = int(minute))
            plan.time_minute = True
            plan.save()
        plan.time = time
        plan.save()

class Create(Helper):
    def post(self, request):
        user = MyUser.objects.get(id__exact = request.user.id)

        # basic info that require in all share options
        name = request.POST.get('plinput')
        des = request.POST.get('pltext')
        image = request.FILES.get('pltfile')
        share = int(request.POST.get('share'))

        # creating plan
        plan = Plan.objects.create(user = user, name = name, des = des, image = image, share = share)

        # add participants
        self.add_participants(plan, request.POST.get('pl_invite'), user)
        
        # add place
        self.add_place(plan, city = request.POST.get('pl_city'), address = request.POST.get('pltpla3_in'))

        # add time
        self.add_time(plan, year=request.POST.get('year'), month = request.POST.get('month'), day = request.POST.get('day'), hour = request.POST.get('hour'), minute = request.POST.get('minute'))

        # add timezone

        self.add_timezone(plan, timezone = request.POST.get('timezone'))
        return HttpResponse('success')

class Join(Helper):
    def get(self, request):
        user = request.user
        plan = Plan.objects.get(pk__exact = int(request.GET.get('key')))
        pp = plan.planparticipants
        try:
            info = ParticipantMoreInfo.objects.create(person = user, planparticipants = pp, plan = plan)
            info.user_invited = True
            info.save()
        except IntegrityError:
            return HttpResponseBadRequest('existed')
        return HttpResponse('success')
