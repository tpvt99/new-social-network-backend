from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.views.generic import View
from .models import Activity, ActivitySport, ActivityParticipants,ActivityEsport, ActivityMusic, ActivityReport
from .models import ActivityPost as ActivityPostModel
from .models import ActivityPostComment as ActivityPostCommentModel
import datetime
from django.utils import timezone
from django.db.utils import IntegrityError
import json
from friend.models import Friend
from django.db.models import Q
from noti.models import Notification, ANotification
from django.core.urlresolvers import reverse
from user.models import MyUser
from noti.models import Notification, ActivityANotification, ActivityBNotification, ActivityCNotification, ActivityDNotification, ActivityNotification, ActivityENotification, ActivityFNotification, ActivityGNotification, ActivityHNotification, ActivityINotification, ActivityJNotification, ActivityKNotification
from status.models import Status
from activities.models import ActivitiesPost
from group.models import Group
import re

# Create your views here.

class Helper(View):
    def age(self, activity, age1, age2):
        if age1 and age2:
            try:
                age1 = int(age1)
                age2 = int(age2)
            except ValueError:
                return False
            if age1 <= age2:
                activity.age1 = age1
                activity.age2 = age2
                return True
            return False
        else:
            return False
    def gettime(self, activity, year, month, day, hour, minute, tz):
        if year and month and day and hour and minute and tz:
            try:
                year = int(year)
                month = int(month)
                day = int(day)
                hour = int(hour)
                minute = int(minute)
                tz= int(tz)
            except ValueError:
                return False
            timex = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute, second = 0, microsecond = 0)
            time_delta = datetime.timedelta(hours = tz)
            timex = timex - time_delta
            timex = timezone.make_aware(timex)
            return timex
        else:
            return False
        
    def sex(self, activity, sex):
        if sex == 'male' or sex == 'female' or sex == 'both':
            activity.sex = sex
            activity.save()
            return True
        return False

    def privacy(self, activity, privacy):
        if privacy == 'private' or privacy == 'public':
            activity.privacy = privacy
            activity.save()
            return True
        return False

    def fee(self, activity, is_free, fee):
        if is_free == 'yes':
            activity.fee = 0
            activity.save()
        elif is_free == 'no':
            try:
                activity.fee = int(fee)
                if activity.fee == 0:
                    raise ValueError
                activity.save()
            except ValueError:
                return False
        else:
            return False
        return True

    def quantity(self, activity, is_limited, quantity):
        if is_limited == 'unlimited':
           activity.quantity = 0
           activity.save()
        elif is_limited == 'limited':
            try:
                quantity = int(quantity)
                if quantity == 0:
                    raise ValueError
                activity.quantity = quantity
                activity.save()
            except ValueError:
                return False
        else:
            return False
        return True

    def activity_type(self, activity, typex):
        list_type = ['sport', 'esport','volunteer','clb','entertainment','backpacking','sing','camp','exchange']
        if typex in list_type:
            activity.activity_type = typex
            activity.save()
            return True
        return False

    def head_verify(self,head):
        r = re.compile(r'[\w ]+')
        t = r.search(head)
        if head == t.group():
            return True
        return False

class CreateActivity(Helper):
    template = 'activity/create.html'
    template1 = 'activity/create_content.html'
    def get(self, request):
        x = request.GET.get('type')
        if x:
            return render(request, self.template1,{'type':x})
        else:
            return render(request, self.template)

    def post(self, request):
        if request.is_ajax():
            image = request.FILES.get('c_img_in')
            privacy = request.POST.get('privacy')
            tz = request.POST.get('timezone')
            typex = request.POST.get('type')
            head = request.POST.get('c_main_in')
            des = request.POST.get('c_d_t')
            age_begin = request.POST.get('beg_a')
            age_end = request.POST.get('end_a')
            sex = request.POST.get('sex')
            who_organize = request.POST.get('who-organize')
            groupid = request.POST.get('group-id')
            year,month,day,hour,minute = request.POST.get('year'), request.POST.get('month'),request.POST.get('day'),request.POST.get('hour'),request.POST.get('minute')
            year_e,month_e,day_e,hour_e,minute_e = request.POST.get('year_e'), request.POST.get('month_e'),request.POST.get('day_e'),request.POST.get('hour_e'),request.POST.get('minute_e')
            province = request.POST.get('province')
            province_unicode = request.POST.get('province_unicode')
            city = request.POST.get('city_unicode')
            address = request.POST.get('c_p_in2')
            is_free = request.POST.get('money')
            fee = request.POST.get('c_mi_in')
            is_limited = request.POST.get('quantity')
            quantity = request.POST.get('c_qi_i')
            if not self.head_verify(head.strip()):
                return HttpResponse(JsonResponse({'a':'error','id':'error9'}))
            if who_organize == 'user':
                activity = Activity.objects.create(user = request.user, image = image, head = head.strip(), des = des, province = province, city = city, address = address, province_unicode = province_unicode)
            else:
                try:
                    group = Group.objects.get(id__exact = int(groupid))
                except:
                    return HttpResponse(JsonResponse({'a':'error','id':'error10'}))
                activity = Activity.objects.create(user = request.user, group = group, image = image, head = head.strip(), des = des, province = province, city = city, address = address, province_unicode = province_unicode)
            if self.sex(activity, sex) and self.privacy(activity, privacy) and self.activity_type(activity, typex):
                pass
            else:
                activity.delete()
                return HttpResponse(JsonResponse({'a':'error','id':'error1'}))
            if self.age(activity, age_begin, age_end):
                pass
            else:
                activity.delete()
                return HttpResponse(JsonResponse({'a':'error','id':'error2'}))
            time_begin = self.gettime(activity, year, month, day, hour, minute, tz)
            time_end = self.gettime(activity, year_e, month_e, day_e, hour_e, minute_e, tz)
            if time_begin and time_end:
                if time_end > time_begin:
                    activity.time_begin = time_begin
                    activity.time_end = time_end
                    activity.timezone = int(tz)
                    activity.save()
                else:
                    activity.delete()
                    return HttpResponse(JsonResponse({'a':'error','id':'error3'}))
            else:
                activity.delete()
                return HttpResponse(JsonResponse({'a':'error','id':'error4'}))
            if self.fee(activity, is_free, fee) and self.quantity(activity, is_limited, quantity):
                pass
            else:
                activity.delete()
                return HttpResponse(JsonResponse({'a':'error','id':'error5'}))
            if typex == 'sport':
                try:
                    actsport = ActivitySport.objects.get(type_of_sport__exact = request.POST.get('c_sport'))
                except ActivitySport.DoesNotExist:
                    actsport = ActivitySport.objects.create(type_of_sport = request.POST.get('c_sport'), type_of_sport_unicode = request.POST.get('type_of_sport_unicode'))
                actsport.activity.add(activity)
            elif typex == 'esport':
                try:
                    actesport = ActivityEsport.objects.get(type_of_esport__exact = request.POST.get('c_esport'))
                except ActivityEsport.DoesNotExist:
                    actesport = ActivityEsport.objects.create(type_of_esport = request.POST.get('c_esport'), type_of_esport_unicode = request.POST.get('type_of_esport_unicode'))
                actesport.activity.add(activity)
            elif typex == 'sing':
                try:
                    actmusic = ActivityMusic.objects.get(type_of_music__exact = request.POST.get('c_music'))
                except ActivityMusic.DoesNotExist:
                    actmusic = ActivityMusic.objects.create(type_of_music = request.POST.get('c_music'), type_of_music_unicode = request.POST.get('type_of_music_unicode'))
                actmusic.activity.add(activity)
            actparti = ActivityParticipants.objects.create(person = request.user, activity = activity, accepted = True)
            noti = Notification.objects.create(user = request.user, noti_type = 'activity')
            ActivityNotification.objects.create(noti = noti,activity = activity)
            des = {'a':'ok','id':activity.id,'head':'-'.join(activity.head.split(' '))}
            response = JsonResponse(des)
        return HttpResponse(response)

class SearchFilter(Helper):
    template = 'activity/search_content.html'
    def post(self, request):
        if request.is_ajax():
            data = request.POST.get('data')
            if data:
                data = json.loads(data)
            else:
                return HttpResponse('error')
            #filter type
            if data.get('type') == 'sport':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), activity_activitysport_activity__type_of_sport__icontains = data.get('sport'), privacy__exact = 'public')
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'esport':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), activity_activityesport_activity__type_of_esport__icontains = data.get('esport'), privacy__exact = 'public')
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'sing':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), activity_activitymusic_activity__type_of_music__icontains = data.get('music'), privacy__exact = 'public')
                except:
                    return HttpResponse('error')
            elif data.get('type') and data.get('type') != 'all':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), privacy__exact = 'public')
                except:
                    return HttpResponse('error')
            else:
                activity = Activity.objects.filter(privacy__exact = 'public')
            # filter SEX
            if data.get('sex') == 'male' or data.get('sex') == 'female':
                activity = activity.filter(sex__exact = data.get('sex'))
            #filter PROVINCE
            if data.get('province').strip() != '':
                activity = activity.filter(province__exact = data.get('province'))
            #filter FEE 
            if data.get('fee') == 'free':
                activity = activity.filter(fee=0)
            elif data.get('fee') == 'nofree':
                activity = activity.exclude(fee=0)
            else:
                pass
            #filter AGE
            age = data.get('age')
            if age == 'kid':
                activity = activity.filter(Q(age1__gte = 5)&Q(age1__lt = 10)|Q(age2__gte=5)&Q(age2__lt=10))
            elif age == 'teen':
                activity = activity.filter(Q(age1__gte = 10)&Q(age1__lt = 20)|Q(age2__gte=10)&Q(age2__lt=20))
            elif age == 'young':
                activity = activity.filter(Q(age1__gte = 20)&Q(age1__lt = 30)|Q(age2__gte=20)&Q(age2__lt=30))
            elif age == 'aldult':
                activity = activity.filter(Q(age1__gte = 30)&Q(age1__lt = 40)|Q(age2__gte=30)&Q(age2__lt=40))
            elif age == 'aged':
                activity = activity.filter(Q(age1__gte = 40)&Q(age1__lt = 55)|Q(age2__gte=40)&Q(age2__lt=55))
            else:
                pass
            #filter QUANTITY
            quantity = data.get('quantity')
            if quantity == 'unlimited':
                activity = activity.filter(quantity = 0)
            elif quantity == 'limited':
                activity = activity.exclude(quantity = 0)
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
                activity = activity.filter((Q(time_begin__gte=beg_time)&Q(time_begin__lte = end_time))|(Q(time_end__gte = beg_time)&Q(time_end__lte = end_time)))
            else:
                activity = activity.filter(Q(time_begin__lte = now)&Q(time_end__gte = now) | Q(time_begin__gte = now))
            return render(request, self.template, {'activity':activity,'head':data.get('head')})
        else:
            data = request.POST
            #filter type
            if data.get('type') == 'sport':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), activity_activitysport_activity__type_of_sport__icontains = data.get('m_op_which'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'esport':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), activity_activityesport_activity__type_of_esport__icontains = data.get('m_op_which'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'sing':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), activity_activitymusic_activity__type_of_music__icontains = data.get('m_op_which'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') != 'all':
                try:
                    activity = Activity.objects.filter(activity_type__icontains = data.get('type'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            else:
                activity = Activity.objects.filter(privacy__exact = 'public', head__icontains = data.get('m_op_head'))
            #filter PROVINCE
            if data.get('m_op_place') != '':
                activity = activity.filter(province__exact = data.get('m_op_place'))
            #filter SEX
            if data.get('sex') == 'male' or data.get('sex') == 'female':
                activity = activity.filter(sex__exact = data.get('sex'))
            #filter FEE 

            if data.get('fee') == 'free':
                activity = activity.filter(fee=0)
            elif data.get('fee') == 'paid':
                activity = activity.exclude(fee=0)
            else:
                pass
            #filter AGE
            age = data.get('age')
            if age == 'kid':
                activity = activity.filter(Q(age_begin__gte = 5)&Q(age_begin__lt = 10)|Q(age_end__gte=5)&Q(age_end__lt=10))
            elif age == 'teen':
                activity = activity.filter(Q(age_begin__gte = 10)&Q(age_begin__lt = 20)|Q(age_end__gte=10)&Q(age_end__lt=20))
            elif age == 'young':
                activity = activity.filter(Q(age_begin__gte = 20)&Q(age_begin__lt = 30)|Q(age_end__gte=20)&Q(age_end__lt=30))
            elif age == 'aldult':
                activity = activity.filter(Q(age_begin__gte = 30)&Q(age_begin__lt = 40)|Q(age_end__gte=30)&Q(age_end__lt=40))
            elif age == 'aged':
                activity = activity.filter(Q(age_begin__gte = 40)&Q(age_begin__lt = 55)|Q(age_end__gte=40)&Q(age_end__lt=55))
            else:
                pass
            #filter QUANTITY
            quantity = data.get('quantity')
            if quantity == 'unlimited':
                activity = activity.filter(quantity = 0)
            elif quantity == 'limited':
                activity = activity.exclude(quantity = 0)
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
                activity = activity.filter((Q(time_begin__gte=beg_time)&Q(time_begin__lte = end_time))|(Q(time_end__gte = beg_time)&Q(time_end__lte = end_time)))
            else:
                activity = activity.filter(Q(time_begin__lte = now)&Q(time_end__gte = now) | Q(time_begin__gte = now))
            return render(request, 'search/search_activity.html', {'activity':activity, 'head':data.get('m_op_head')})

class Join(Helper):
    def post(self, request):
        try:
            activity = Activity.objects.get(pk__exact = int(request.POST.get('act')))
        except Activity.DoesNotExist:
            return HttpResponse('error')
        if request.POST.get('action') == 'join':
            try:
                ap = ActivityParticipants.objects.get(person = request.user, activity = activity)
                return HttpResponse('error')
            except ActivityParticipants.DoesNotExist:
                ap = ActivityParticipants.objects.create(person = request.user, activity = activity, accepted = False, guess_invite = True)
                noti = Notification.objects.create(user = activity.user, noti_type = 'activity-a')
                ActivityANotification.objects.create(noti = noti, activityparticipants = ap)
                return HttpResponse('ok')
        elif request.POST.get('action') == 'invite':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            try:
                ap = ActivityParticipants.objects.get(person = user, activity = activity)
                return HttpResponse('error')
            except ActivityParticipants.DoesNotExist:
                ap = ActivityParticipants.objects.create(person = user, activity = activity, accepted = False, owner_invite = True)
                noti = Notification.objects.create(user = user, noti_type = 'activity-b')
                ActivityBNotification.objects.create(noti = noti, activityparticipants = ap)
                return HttpResponse('ok')
        elif request.POST.get('action') == 'accept':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error3')
            if request.user == activity.user:
                try:
                    ap = ActivityParticipants.objects.get(person = user, activity = activity, accepted = False, guess_invite = True)
                    ap.accepted = True
                    ap.save()
                    noti = Notification.objects.create(user = user, noti_type = 'activity-e')
                    ActivityENotification.objects.create(noti = noti, activityparticipants = ap)
                    return HttpResponse('ok')
                except ActivityParticipants.DoesNotExist:
                    return HttpResponse('error4')
            else:
                try:
                    ap = ActivityParticipants.objects.get(person = request.user, activity = activity, accepted = False, owner_invite = True)
                    ap.accepted = True
                    ap.save()
                    noti = Notification.objects.create(user =activity.user, noti_type = 'activity-f')
                    ActivityFNotification.objects.create(noti = noti, activityparticipants = ap)
                    return HttpResponse('ok')
                except ActivityParticipants.DoesNotExist:
                    return HttpResponse('error')
        elif request.POST.get('action') == 'decline':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            if request.user == activity.user:
                try:
                    ap = ActivityParticipants.objects.get(person = user, activity = activity, accepted = False, owner_invite = True)
                    try:
                        zz = ActivityBNotification.objects.get(activityparticipants = ap)
                        zz.noti.delete()
                    except ActivityBNotification.DoesNotExist:
                        pass
                    noti = Notification.objects.create(user = user, noti_type = 'activity-c')
                    ActivityCNotification.objects.create(noti = noti, activity = activity, time_send = ap.time_create)
                    ap.delete()
                    return HttpResponse('ok')
                except ActivityParticipants.DoesNotExist:
                    return HttpResponse('error')
            else:
                try:
                    ap = ActivityParticipants.objects.get(person = request.user, activity = activity, accepted = False, guess_invite = True)
                    try:
                        zz = ActivityANotification.objects.get(activityparticipants = ap)
                        zz.noti.delete()
                    except ActivityANotification.DoesNotExist:
                        pass
                    noti = Notification.objects.create(user = activity.user, noti_type = 'activity-d')
                    ActivityDNotification.objects.create(noti = noti, activity=activity, guess=request.user, time_send = ap.time_create)
                    ap.delete()
                    return HttpResponse('ok')
                except ActivityParticipants.DoesNotExist:
                    return HttpResponse('error')
        elif request.POST.get('action') == 'refuse':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            if activity.user == request.user:
                try:
                    ap = ActivityParticipants.objects.get(person = user,  activity= activity, accepted = False, guess_invite = True)
                    try:
                        zz = ActivityANotification.objects.get(activityparticipants = ap)
                        zz.noti.delete()
                    except ActivityANotification.DoesNotExist:
                        pass
                    ap.delete()
                    noti = Notification.objects.create(user = user, noti_type='activity-g')
                    ActivityGNotification.objects.create( activity= activity, noti = noti)
                    return HttpResponse('ok')
                except ActivityParticipants.DoesNotExist:
                    return HttpResponse('error')
            else:
                try:
                    ap = ActivityParticipants.objects.get(person = request.user, activity= activity, accepted = False, owner_invite = True)
                    try:
                        zz = ActivityBNotification.objects.get(activityparticipants = ap)
                        zz.noti.delete()
                    except ActivityBNotification.DoesNotExist:
                        pass
                    ap.delete()
                    noti = Notification.objects.create(user = activity.user, noti_type='activity-h')
                    ActivityHNotification.objects.create( activity= activity, noti = noti ,guess=request.user)
                    return HttpResponse('ok')
                except ActivityParticipants.DoesNotExist:
                    return HttpResponse('error')
        elif request.POST.get('action') == 'report':
            try:
                ActivityReport.objects.create(activity=activity, user = request.user)
                activity.report += 1
                activity.save()
                noti = Notification.objects.create(user =activity.user, noti_type = 'activity-i')
                ActivityINotification.objects.create(noti = noti, activity=activity)
                return HttpResponse('ok')
            except IntegrityError:
                return HttpResponse('error')

class ActivityView(Helper):
    template = 'activity/activity.html'
    def get(self, request, *a, **kw):
        x = kw.get('id')
        head = kw.get('head')
        idx = request.GET.get('id')
        if x and head:
            try:
                x = int(x)
                head = ' '.join(head.split('-'))
            except ValueError:
                return HttpResponseRedirect(reverse('web:webpage'))
            except AttributeError:
                return HttpResponseRedirect(reverse('web:webpage'))
            try:
                activity = Activity.objects.get(pk__exact = x, head=head)
            except Activity.DoesNotExist:
                return HttpResponseRedirect(reverse('web:webpage'))
            ap = activity.activity_activityparticipants_activity.filter(accepted = True)
            for i in ap:
                if request.user == i.person:
                    if idx and int(idx):
                        if request.user.id == int(idx):
                            activitiespost = ActivitiesPost.objects.filter(user = request.user, activity = activity).order_by('-time_create')
                            ttt = []
                            for i in activitiespost:
                                if i.status_set.all():
                                    ttt.append(i.status_set.all()[0])
                            return render(request, 'activities/myown_activity.html', {'activity':activity, 'status':ttt})
                    friends = Friend.objects.filter(user = request.user)
                    activitypost = Status.objects.filter(activitypost__activity = activity, user = activity.user).order_by('-time_create')
                    return render(request, self.template, {'activity':activity,'friends':friends,'value':activity.id,'status':activitypost})
            return HttpResponseRedirect('/activity/activity/link/'+'?id='+str(activity.id))
        else:
            return HttpResponseRedirect(reverse('web:webpage'))


class ActivityViewAll(View):
    template = 'activity/activity_view_all.html'
    def get(self, request):
        organize = Activity.objects.filter(user = request.user)
        join_accepted = Activity.objects.filter(activity_activityparticipants_activity__person = request.user, activity_activityparticipants_activity__accepted = True).exclude(user = request.user)
        join_wait = Activity.objects.filter(activity_activityparticipants_activity__person = request.user, activity_activityparticipants_activity__accepted = False).exclude(user = request.user)
        return render(request, self.template ,{'organize':organize,'join_accepted':join_accepted,'join_wait':join_wait})

class SpecificContent(View):
    def get(self, request):
        x = request.GET.get('id')
        activity = Activity.objects.filter(pk = int(x))
        return render(request, 'activity/specific_content.html',{'activity':activity})

class ActivityPost(View):
    template = 'activity/activitystatus_render.html'
    def post(self, request):
        try:
            activity = Activity.objects.get(pk__exact = request.POST.get('id'))
        except Acivity.DoesNotExist:
            raise Http404('error')
        ap = activity.activity_activityparticipants_activity.filter(accepted = True)
        if request.user == activity.user:
            activitypost = ActivityPostModel.objects.create(activity = activity, user =request.user, text = request.POST.get('act_des'))
            if request.FILES.get('image'):
                activitypost.image = request.FILES.get('image')
                activitypost.save()
            ttt = []
            for i in ap:
                noti = Notification.objects.create(user = i.person, noti_type = 'activity-j')
                ActivityJNotification.objects.create(noti = noti, activity = activity, user = request.user)
            status = Status.objects.create(status_type = 'activitypost', activitypost = activitypost, activity = activity, privacy = 'activity')
            ttt.append(status)

            return render(request, 'status/status.html',{'status':ttt})
        else:
            return HttpResponse('error')

class ActivityPostComment(View):
    template = 'activity/activitypostcomment_render.html'
    def post(self,request):
        try:
            activitypost = ActivityPostModel.objects.get(id__exact = request.POST.get('id'))
        except ActivityPostModel.DoesNotExist:
            return HttpResponse('error')
        activitypostcomment = ActivityPostCommentModel.objects.create(activitypost = activitypost, user = request.user, comment = request.POST.get('comment'))
        noti = Notification.objects.create(user = activitypost.user ,noti_type = 'activity-k')
        ActivityKNotification.objects.create(noti = noti, activitypostcomment = activitypostcomment)
        return render(request, self.template, {'comment':activitypostcomment})

