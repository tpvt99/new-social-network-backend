from django.shortcuts import render
from django.views.generic import View

from .models import Contest as ContestModel
from .models import ContestPost as ContestPostModel
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import re
import datetime
from django.utils import timezone
from noti.models import Notification, ContestNotification, ContestANotification
from django.db.models import Q
import json
from .models import ContestFollow
from django.db.utils import IntegrityError
from status.models import Status

# Create your views here.

class Helper(View):
    def head_validate(self, head):
        x = re.compile(r'[\w ]+')
        if head == x.search(head).group():
            head = head.strip()
            return ' '.join(head.split('_'))
        return False

    def age(self, contest,age_begin,age_end):
        try:
            age_begin = int(age_begin)
            age_end = int(age_end)
            if age_begin > age_end:
                raise ValueError
            contest.age_begin = age_begin
            contest.age_end = age_end
            contest.save()
            return True
        except ValueError:
            return False

    def gettime(self, year, month, day, hour, minute, tz):
        if year and month and day and hour and minute and tz:
            try:
                year = int(year)
                month = int(month)
                day = int(day)
                hour = int(hour)
                minute = int(minute)
                tz= int(tz)
            except ValueError:
                print('error1')
                return False
            timex = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute, second = 0, microsecond = 0)
            time_delta = datetime.timedelta(hours = tz)
            timex = timex - time_delta
            timex = timezone.make_aware(timex)
            return timex
        else:
            print('error2')
            return False

class Create(Helper):
    template = 'contest/create.html'
    def get(self, request):
        return render(request, self.template)
    def post(self, request):
        data = request.POST
        head = self.head_validate(data.get('head'))
        if head:
            contest = ContestModel.objects.create(head = head, des = data.get('des'), image = request.FILES.get('image'), user = request.user)
        else :
            raise Http404('head error')
        if self.age(contest, data.get('age_begin'), data.get('age_end')):
            pass
        else:
            contest.delete()
            raise Http404('age error')
        contest.timezone = int(data.get('timezone')) 
        contest.contest_type = data.get('type')
        contest.province = data.get('province')
        contest.province_unicode = data.get('province_unicode')
        contest.save()
        time_begin = self.gettime(data.get('year'),data.get('month'),data.get('day'),data.get('hour'),data.get('minute'), tz = data.get('timezone'))
        if time_begin != False:
            contest.time_begin = time_begin
            contest.save()
        else:
            contest.delete()
            raise Http404('time error')
        if data.get('privacy') == 'public' or data.get('privacy') == 'private':
            contest.privacy = data.get('privacy')
            contest.save()
        else:
            contest.delete()
            raise Http404('privacy error')
        ContestFollow.objects.create(contest = contest, user = request.user)
        noti = Notification.objects.create(user = request.user, noti_type='contest')
        ContestNotification.objects.create(noti = noti, contest = contest)
        return HttpResponseRedirect(reverse('contest:contest', args=[contest.id, '-'.join(head.split(' '))]))
    

class ContestViewAll(View):
    template = 'contest/contest_view_all.html'
    def get(self, request):
        organize = ContestModel.objects.filter(user = request.user)
        join = ContestModel.objects.filter(contest_contestfollow_contest__user = request.user).exclude(user = request.user)
        return render(request, self.template, {'organize':organize,'join':join})


class ContestView(View):
    template = 'contest/contest.html'
    def get(self, request, *a, **kw):
        x = kw.get('id')
        head = kw.get('head')
        if x and head:
            try:
                x = int(x)
                head = ' '.join(head.split('-'))
            except ValueError:
                return HttpResponseRedirect(reverse('web:webpage'))
            except AttributeError:
                return HttpResponseRedirect(reverse('web:webpage'))
            try:
                contest = ContestModel.objects.get(pk__exact = x, head=head)
                contestpost = contest.contest_contestpost_contest.all()
            except ContestModel.DoesNotExist:
                return HttpResponseRedirect(reverse('web:webpage'))
            return render(request, self.template, {'contest':contest,'value':contest.id,'contestpost':contestpost})
        else:
            return HttpResponseRedirect(reverse('web:webpage'))

class ContestPost(View):
    template = 'status/status.html'
    def post(self, request):
        try:
            contest = ContestModel.objects.get(pk__exact = request.POST.get('id'))
        except Contest.DoesNotExist:
            return HttpResponse('error')
        contestpost = ContestPostModel.objects.create(user = request.user, contest = contest, text = request.POST.get('cont_des'))
        if request.FILES.get('image'):
            contestpost.image = request.FILES.get('image')
            contestpost.save()
        followers = ContestFollow.objects.filter(contest = contest)
        Status.objects.create(contest=contest, status_type="contest-post", privacy="contest", contestpost = contestpost)
        for i in followers:
            if i.user != contest.user:
                noti = Notification.objects.create(user = i.user, noti_type="contest-a")
                ContestANotification.objects.create(noti = noti, contestpost = contestpost)
        return render(request, self.template,{'post':contestpost})

class Follow(View):
    def get(self, request):
        user = request.user
        action = request.GET.get('action')
        try:
            contest = ContestModel.objects.get(id__exact = int(request.GET.get('contest')))
        except:
            return HttpResponse('error')
        if action == 'interest':
            try:
                ContestFollow.objects.create(contest = contest, user = user)
            except IntegrityError:
                return HttpResponse('error')
        else:
            return HttpResponse('error')
        return HttpResponse('ok')

class SearchFilter(View):
    template = 'contest/search_content.html'
    def post(self, request):
        if request.is_ajax():
            print(request.POST.get('data'))
            data = request.POST.get('data')
            if data:
                data = json.loads(data)
            else:
                return HttpResponse('error')
            #filter type
            if data.get('type') and data.get('type') != 'all':
                try:
                    contest = ContestModel.objects.filter(contest_type__icontains = data.get('type'), privacy__exact = 'public')
                except:
                    return HttpResponse('error')
            else:
                contest = ContestModel.objects.filter(privacy__exact = 'public', head__icontains = data.get('head'))
            #filter PROVINCE
            if data.get('province') != '':
                contest = contest.filter(province__exact = data.get('province'))
            #filter FEE 
            if data.get('fee') == 'free':
                contest = contest.filter(fee=0)
            elif data.get('fee') == 'paid':
                contest = contest.exclude(fee=0)
            else:
                pass
            #filter AGE
            age = data.get('age')
            if age == 'kid':
                contest = contest.filter(Q(age_begin__gte = 5)&Q(age_begin__lt = 10)|Q(age_end__gte=5)&Q(age_end__lt=10))
            elif age == 'teen':
                contest = contest.filter(Q(age_begin__gte = 10)&Q(age_begin__lt = 20)|Q(age_end__gte=10)&Q(age_end__lt=20))
            elif age == 'young':
                contest = contest.filter(Q(age_begin__gte = 20)&Q(age_begin__lt = 30)|Q(age_end__gte=20)&Q(age_end__lt=30))
            elif age == 'aldult':
                contest = contest.filter(Q(age_begin__gte = 30)&Q(age_begin__lt = 40)|Q(age_end__gte=30)&Q(age_end__lt=40))
            elif age == 'aged':
                contest = contest.filter(Q(age_begin__gte = 40)&Q(age_begin__lt = 55)|Q(age_end__gte=40)&Q(age_end__lt=55))
            else:
                pass
            #filter QUANTITY
            quantity = data.get('quantity')
            if quantity == 'unlimited':
                contest = contest.filter(quantity = 0)
            elif quantity == 'limited':
                contest = contest.exclude(quantity = 0)
            else:
                pass
            #filter TIME
            wtime = data.get('time')
            tz = int(data.get('timezone'))
            now = timezone.now()
            if tz > 0:
                if now.hour > (24 - tz):
                    beg_time = now.replace(hour = 24-tz,minute=0,second=0,microsecond=0)
                else:
                    beg_time = now.replace(hour = 24 - tz,minute = 0,second=0,microsecond=0) + datetime.timedelta(days=-1)
            elif tz < 0:
                if now.hour > abs(tz):
                    beg_time = now.replace(hour = abs(tz),minute=0,second=0,microsecond=0)
                else:
                    beg_time = now.replace(hour = abs(tz),minute=0,second=0,microsecond=0) + datetime.timedelta(days=-1)
            else:
                beg_time = now.replace(minute =0,second=0,microsecond=0)
            if wtime != 'all':
                if wtime == 'today':
                    end_time = beg_time + datetime.timedelta(hours = 24)
                elif wtime == 'tomorrow':
                    beg_time = beg_time + datetime.timedelta(hours = 24)
                    end_time = beg_time + datetime.timedelta(hours = 24)
                elif wtime == 'nextday':
                    beg_time = beg_time + datetime.timedelta(hours = 24*2)
                    end_time = beg_time + datetime.timedelta(hours = 24)
                elif wtime == 'week':
                    beg_time = beg_time + datetime.timedelta(days = now.day -now.weekday())
                    end_time = beg_time + datetime.timedelta(hours = 24*7)
                elif wtime == 'nextweek':
                    beg_time = beg_time + datetime.timedelta(days = now.day + 7-now.weekday())
                    end_time = beg_time + datetime.timedelta(hours = 24*7)
                contest = contest.filter((Q(time_begin__gte=beg_time)&Q(time_begin__lte = end_time))|(Q(time_end__gte = beg_time)&Q(time_end__lte = end_time)))
            else:
                contest = contest.filter(time_begin__gte = now)
            return render(request, self.template, {'contests':contest, 'head':data.get('head')})
        else:
            data = request.POST
            #filter type
            if data.get('m_op_which') == '':
                contest = ContestModel.objects.filter(privacy = 'public', head__icontains = data.get('m_op_head'))
            else:
                contest = ContestModel.objects.filter(privacy = 'public', head__icontains = data.get('m_op_head'), contest_type = data.get('m_op_which'))
            #filter PROVINCE
            if data.get('m_op_place') != '':
                contest = contest.filter(province__exact = data.get('m_op_place'))
            #filter AGE
            age = data.get('age')
            if age == 'kid':
                contest = contest.filter(Q(age_begin__gte = 5)&Q(age_begin__lt = 10)|Q(age_end__gte=5)&Q(age_end__lt=10))
            elif age == 'teen':
                contest = contest.filter(Q(age_begin__gte = 10)&Q(age_begin__lt = 20)|Q(age_end__gte=10)&Q(age_end__lt=20))
            elif age == 'young':
                contest = contest.filter(Q(age_begin__gte = 20)&Q(age_begin__lt = 30)|Q(age_end__gte=20)&Q(age_end__lt=30))
            elif age == 'aldult':
                contest = contest.filter(Q(age_begin__gte = 30)&Q(age_begin__lt = 40)|Q(age_end__gte=30)&Q(age_end__lt=40))
            elif age == 'aged':
                contest = contest.filter(Q(age_begin__gte = 40)&Q(age_begin__lt = 55)|Q(age_end__gte=40)&Q(age_end__lt=55))
            else:
                pass
            #filter TIME
            wtime = data.get('time')
            tz = int(data.get('timezone'))
            now = timezone.now()
            if tz > 0:
                if now.hour > (24 - tz):
                    beg_time = now.replace(hour = 24-tz,minute=0,second=0,microsecond=0)
                else:
                    beg_time = now.replace(hour = 24 - tz,minute = 0,second=0,microsecond=0) + datetime.timedelta(days=-1)
            elif tz < 0:
                if now.hour > abs(tz):
                    beg_time = now.replace(hour = abs(tz),minute=0,second=0,microsecond=0)
                else:
                    beg_time = now.replace(hour = abs(tz),minute=0,second=0,microsecond=0) + datetime.timedelta(days=-1)
            else:
                beg_time = now.replace(minute =0,second=0,microsecond=0)
            if wtime != 'all':
                if wtime == 'today':
                    end_time = beg_time + datetime.timedelta(hours = 24)
                elif wtime == 'tomorrow':
                    beg_time = beg_time + datetime.timedelta(hours = 24)
                    end_time = beg_time + datetime.timedelta(hours = 24)
                elif wtime == 'nextday':
                    beg_time = beg_time + datetime.timedelta(hours = 24*2)
                    end_time = beg_time + datetime.timedelta(hours = 24)
                elif wtime == 'week':
                    beg_time = beg_time + datetime.timedelta(days = now.day -now.weekday())
                    end_time = beg_time + datetime.timedelta(hours = 24*7)
                elif wtime == 'nextweek':
                    beg_time = beg_time + datetime.timedelta(days = now.day + 7-now.weekday())
                    end_time = beg_time + datetime.timedelta(hours = 24*7)
                contest = contest.filter((Q(time_begin__gte=beg_time)&Q(time_begin__lte = end_time)))
            else:
                contest = contest.filter(Q(time_begin__lte = now) | Q(time_begin__gte = now))
            return render(request, 'search/search_contest.html', {'contests':contest, 'head':data.get('m_op_head')})
