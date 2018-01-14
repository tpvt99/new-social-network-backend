from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import View
from django.utils import timezone
from datetime import timedelta

from .models import Diary

# Create your views here.

class Create(View):
    template = 'web/right_diary.html'
    def post(self, request):
        image = request.FILES.get('ld_im')
        text = request.POST.get('ld_t')
        timezone = int(request.POST.get('timezone'))
        diary = Diary.objects.create(user = request.user, diary = text, image =image, timezone = timezone)
        return render(request, self.template, {'diary':diary, 'tz':timezone})

class Content(View):
    template = 'web/right_diary.html'
    def get(self, request):
        tz = int(request.GET.get('tz'))
        if tz >= 0:
            delta = timedelta(hours = tz)
            begin_day = timezone.now() + delta
            begin_day = begin_day.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
            begin_day = begin_day - delta
            end_day = begin_day + timedelta(hours = 24)
        else:
            delta = timedelta(hours = abs(tz))
            begin_day = timezone.now() - delta
            begin_day = begin_day.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
            begin_day = begin_day + delta
            end_day = begin_day + timdelta(hours = 24)
        diaries = Diary.objects.filter(user = request.user, create_time__gte = begin_day, create_time__lte = end_day)
        return render(request, self.template, {'diaries':diaries, 'tz':tz})
