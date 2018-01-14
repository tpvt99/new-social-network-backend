from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
import json
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Scholarship, ScholarshipTarget

# Create your views here.

class Helper(View):
    def time_begin(self, scholarship, time):
        year = time.get('year')
        month = time.get('month')
        day = time.get('day')
        hour = time.get('hour')
        minute = time.get('minute')
        if year.strip() and month.strip() and day.strip() and hour.strip() and minute.strip():
            try:
                dt = datetime(year = int(year), month = int(month), day = int(day), hour = int(hour), minute = int(minute))
                dt = timezone.make_aware(dt - timedelta(hours = scholarship.timezone))
                scholarship.time_begin = dt
                scholarship.save()
                return True
            except ValueError:
                return False
        else:
            return False

    def time_end(self, scholarship, time):
        year = time.get('year')
        month = time.get('month')
        day = time.get('day')
        hour = time.get('hour')
        minute = time.get('minute')
        if year.strip() and month.strip() and day.strip() and hour.strip() and minute.strip():
            try:
                dt = datetime(year = int(year), month = int(month), day = int(day), hour = int(hour), minute = int(minute))
                dt = timezone.make_aware(dt - timedelta(hours = scholarship.timezone))
                scholarship.time_end = dt
                scholarship.save()
                return True
            except ValueError:
                return False
        else:
            return False

    def timezone(self, scholarship, timezone):
        scholarship.timezone = timezone
        scholarship.save()
        return True

    def prize(self, scholarship, prize):
        if prize:
            scholarship.prize = prize
            scholarship.save()
            return True
        else:
            return False
    
    def content(self, scholarship, content):
        if content:
            scholarship.content = content
            scholarship.save()
            return True
        else:
            return False

    def target_des(self, scholarship, des):
        if des:
            scholarship.target_des = des
            scholarship.save()
            return True
        else:
            return False

    def target(self, scholarship, target):
        if target:
            for i in target:
                if i.strip():
                    st = ScholarshipTarget.objects.get(name__exact = i)
                    scholarship.target.add(st)
                else:
                    return False
            return True
        else:
            return False

class Create(Helper):
    template = 'scholarship/create.html'
    def get(self, request):
        return render(request, self.template)
    def post(self, request):
        # change user if there is a page
        data = request.POST.get('data')
        if data.strip():
            data = json.loads(data)
            scholarship = Scholarship.objects.create(user = request.user, head = data.get('head'))
            if self.timezone(scholarship, data.get('timezone')) and self.prize(scholarship, data.get('pri')) and self.content(scholarship, data.get('main')) and self.target_des(scholarship, data.get('target_des')):
                pass
            else:
                scholarship.delete()
                raise Http404('error')
            if self.time_begin(scholarship, data.get('begin_time')) and self.time_end(scholarship, data.get('end_time')):
                pass
            else:
                scholarship.delete()
                raise Http404('error')
            if self.target(scholarship, data.get('target')):
                pass
            else:
                scholarship.delete()
                raise Http404('error')
            return HttpResponse('ok')
        else:
            raise Http404('error')

class Content(Helper):
    template = 'scholarship/search_content.html'
    def post(self, request):
        if request.is_ajax():
            """   # for checkbox button
            target = request.POST.get('data')
            if target:
                target = json.loads(target)
            tz = target.get('timezone')
            target = target.get('target')
            scholarship = []
            if target:
                for i in target:
                    now = timezone.now()
                    st = ScholarshipTarget.objects.get(name__contains=i)
                    sc = Scholarship.objects.filter(time_end__gte = now, target = st)
                    scholarship.extend(list(sc))
            else:
                now = timezone.now()
                sc = Scholarship.objects.filter(time_end__gte = now)
                scholarship.extend(list(sc))
            return render(request, self.template, {'scholarships':scholarship, 'tz':tz})
            """
            data = request.POST.get('data')
            if data:
                data = json.loads(data)
            tz = data.get('timezone')
            target = data.get('target')
            if target and target != 'all':
                now = timezone.now()
                st = ScholarshipTarget.objects.get(name__contains=target)
                sc = Scholarship.objects.filter(time_end__gte = now, target = st)
            else:
                now = timezone.now()
                sc = Scholarship.objects.filter(time_end__gte = now)
            return render(request, self.template, {'scholarships':sc, 'tz':tz})
