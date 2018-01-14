from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
import re, json
import datetime
from django.utils import timezone
from .models import Event as EventModel
from .models import EventMusic, EventSport, EventParticipants, EventReport
from .models import EventPost as EventPostModel
from .models import EventPostComment as EventPostCommentModel
from django.db.utils import IntegrityError
from friend.models import Friend
from django.db.models import Q
from user.models import MyUser
from noti.models import Notification, EventANotification, EventBNotification, EventCNotification, EventDNotification, EventNotification, EventENotification, EventFNotification, EventGNotification, EventHNotification, EventINotification, EventJNotification, EventKNotification
from status.models import Status
from events.models import EventsPost
import re

# Create your views here.

class Helper(View):
    error = []
    def head_validate(self, head):
        x = re.compile(r'[\w ]+')
        if head == x.search(head).group():
            head = head.strip()
            return ' '.join(head.split('_'))
        self.error.append('error head')
        return False

    def age(self, event , age1, age2):
        if age1 and age2:
            try:
                age1 = int(age1)
                age2 = int(age2)
            except ValueError:
                return False
            if age1 <= age2:
                event.age_begin = age1
                event.age_end = age2
                event.save()
                return True
            return False
        else:
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
                self.error.append('error gettime')
                return False
            timex = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute, second = 0, microsecond = 0)
            time_delta = datetime.timedelta(hours = tz)
            timex = timex - time_delta
            timex = timezone.make_aware(timex)
            return timex
        else:
            self.error.append('error gettime')
            return False
        
    def fee(self,event, is_free, fee_des):
        if is_free == 'free':
            event.fee = 0
            event.fee_des = fee_des
            event.save()
        elif is_free == 'paid':
            event.fee = 1
            event.fee_des = fee_des
            event.save()
        else:
            self.error.append('error fee' )
            return False
        return True

    def quantity(self,event, is_limited, quantity):
        if is_limited == 'unlimited':
           event.quantity = 0
           event.save()
        elif is_limited == 'limited':
            try:
                quantity = int(quantity)
                if quantity == 0:
                    self.error.append('error quantity')
                    raise ValueError
                event.quantity = quantity
                event.save()
            except ValueError:
                self.error.append('error quantity')
                return False
        else:
            self.error.append('error quantity')
            return False
        return True

    def type(self,event, typex):
        list_type = ['sport','music','sport','talk','prom','tech','fair']
        if typex in list_type:
            event.event_type = typex
            event.save()
            return True
        self.error.append('error type')
        return False

class CreateEvent(Helper):
    template = 'event/create_content.html'
    def get(self, request):
        a = request.GET.get('type')
        if a:
            return render(request, self.template,{'type':a})
        else:
            return render(request, 'event/create.html')

    def post(self, request):
        head = self.head_validate(request.POST.get('f_b_i1'))
        if not head:
            raise Http404('error')
        des = request.POST.get('f_d_t')
        image = request.FILES.get('f_img')
        if head and des and image:
            event = EventModel.objects.create(head = head, des = des, user = request.user, image = image)
        else:
            raise Http404('error1')
        province,province_unicode,city_unicode,address = request.POST.get('b_c_in'), request.POST.get('province_unicode'), request.POST.get('city_unicode'), request.POST.get('b_c_in1')
        if province and province_unicode and city_unicode and address:
            event.province = province
            event.province_unicode = province_unicode
            event.city_unicode = city_unicode
            event.address = address
            event.save()
        else:
            event.delete()
            raise Http404('error2')
        time_begin = self.gettime(request.POST.get('year'), request.POST.get('month'), request.POST.get('day'), request.POST.get('hour'), request.POST.get('minute'), request.POST.get('timezone'))
        time_end = self.gettime(request.POST.get('year_e'), request.POST.get('month_e'), request.POST.get('day_e'), request.POST.get('hour_e'), request.POST.get('minute_e'), request.POST.get('timezone'))
        if time_begin and time_end:
            if time_end > time_begin:
                event.time_end = time_end
                event.time_begin = time_begin
                event.timezone = int(request.POST.get('timezone'))
                event.save()
            else:
                event.delete()
                raise Http404('error3')
        else:
            event.delete()
            raise Http404('error4')
        event.privacy = request.POST.get('privacy')
        event.save()
        if self.age(event, request.POST.get('beg_a'), request.POST.get('end_a')) and self.fee(event, request.POST.get('fee'), request.POST.get('fee_text')) and self.quantity(event, request.POST.get('quan'), request.POST.get('qu')):
            pass
        else:
            event.delete()
            raise Http404('error5')
        if self.type(event, request.POST.get('type')):
            pass
        else:
            event.delete()
            raise Http404('error')
        typex = request.POST.get('type')
        if typex == 'sport':
            try:
                e = EventSport.objects.get(sport_type = request.POST.get('f_sport'))
            except EventSport.DoesNotExist:
                e = EventSport.objects.create(sport_type = request.POST.get('f_sport'), sport_type_unicode = request.POST.get('f_sport_unicode'))
            e.event.add(event)
        elif typex == 'music':
            try:
                e = EventMusic.objects.get(music_type = request.POST.get('f_music'))
            except EventMusic.DoesNotExist:
                e = EventMusic.objects.create(music_type = request.POST.get('f_music'), music_type_unicode = request.POST.get('f_music_unicode'))
            e.event.add(event)
        ep = EventParticipants.objects.create(user = request.user, event = event, owner_invite = True, accepted = True)
        # create notification
        noti = Notification.objects.create(user = request.user, noti_type='event')
        EventNotification.objects.create(noti = noti, event = event)
        return HttpResponseRedirect(reverse('event:event', args=[event.id, '-'.join(head.split(' '))]))


class EventViewAll(View):
    template = 'event/event_view_all.html'
    def get(self, request):
        organize = EventModel.objects.filter(user = request.user)
        join_accepted = EventModel.objects.filter(event_eventparticipants_event__user = request.user, event_eventparticipants_event__accepted = True).exclude(user = request.user)
        join_wait = EventModel.objects.filter(event_eventparticipants_event__user = request.user, event_eventparticipants_event__accepted = False).exclude(user = request.user)
        return render(request, self.template,{'organize':organize,'join_accepted':join_accepted,'join_wait':join_wait})

class EventView(Helper):
    template = 'event/event.html'
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
                event = EventModel.objects.get(pk__exact = x, head=head)
            except Event.DoesNotExist:
                return HttpResponseRedirect(reverse('web:webpage'))
            ap = event.event_eventparticipants_event.filter(accepted = True)
            for i in ap:
                if request.user == i.user:
                    if idx and int(idx):
                        eventspost = EventsPost.objects.filter(user = request.user, event = event).order_by('-time_create')
                        ttt= []
                        for i in eventspost:
                            if i.status_set.all():
                                ttt.append(i.status_set.all()[0])
                        return render(request, 'events/myown_event.html' ,{'event':event,'status':ttt})
                    friends = Friend.objects.filter(user = request.user)
                    accepted = EventParticipants.objects.filter(event = event, accepted = True)
                    wait = EventParticipants.objects.filter(event = event, accepted = False, guess_invite = True)
                    invite = EventParticipants.objects.filter(event = event, accepted = False, owner_invite = True)
                    eventpost = Status.objects.filter(eventpost__event = event, user = event.user).order_by('-time_create')
                    return render(request, self.template, {'event':event,'friends':friends,'accepted':accepted,'wait':wait,'invite':invite, 'value':event.id,'status':eventpost})
            return HttpResponseRedirect('/event/event/link/'+'?id='+str(event.id))
        else:
            return HttpResponseRedirect(reverse('web:webpage'))


class SearchFilter(Helper):
    template = 'event/search_content.html'
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
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), event_eventsport_event__sport_type__icontains = data.get('sport'), privacy__exact = 'public', head__icontains = data.get('head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'esport':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), event_eventesport_event__esport_type__icontains = data.get('esport'), privacy__exact = 'public', head__icontains = data.get('head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'music':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), event_eventmusic_event__music_type__icontains = data.get('music'), privacy__exact = 'public', head__icontains = data.get('head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') and data.get('type') != 'all':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), privacy__exact = 'public', head__icontains = data.get('head'))
                except:
                    return HttpResponse('error')
            else:
                event = EventModel.objects.filter(privacy__exact = 'public', head__icontains = data.get('head'))
            #filter PROVINCE
            if data.get('province') != '':
                event = event.filter(province__exact = data.get('province'))
            #filter FEE 
            if data.get('fee') == 'free':
                event = event.filter(fee=0)
            elif data.get('fee') == 'paid':
                event = event.exclude(fee=0)
            else:
                pass
            #filter AGE
            age = data.get('age')
            if age == 'kid':
                event = event.filter(Q(age_begin__gte = 5)&Q(age_begin__lt = 10)|Q(age_end__gte=5)&Q(age_end__lt=10))
            elif age == 'teen':
                event = event.filter(Q(age_begin__gte = 10)&Q(age_begin__lt = 20)|Q(age_end__gte=10)&Q(age_end__lt=20))
            elif age == 'young':
                event = event.filter(Q(age_begin__gte = 20)&Q(age_begin__lt = 30)|Q(age_end__gte=20)&Q(age_end__lt=30))
            elif age == 'aldult':
                event = event.filter(Q(age_begin__gte = 30)&Q(age_begin__lt = 40)|Q(age_end__gte=30)&Q(age_end__lt=40))
            elif age == 'aged':
                event = event.filter(Q(age_begin__gte = 40)&Q(age_begin__lt = 55)|Q(age_end__gte=40)&Q(age_end__lt=55))
            else:
                pass
            #filter QUANTITY
            quantity = data.get('quantity')
            if quantity == 'unlimited':
                event = event.filter(quantity = 0)
            elif quantity == 'limited':
                event = event.exclude(quantity = 0)
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
                event = event.filter((Q(time_begin__gte=beg_time)&Q(time_begin__lte = end_time))|(Q(time_end__gte = beg_time)&Q(time_end__lte = end_time)))
            else:
                event = event.filter(Q(time_begin__lte = now)&Q(time_end__gte = now) | Q(time_begin__gte = now))
            return render(request, self.template, {'events':event, 'head':data.get('head')})
        else:
            data = request.POST
            #filter type
            if data.get('type') == 'sport':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), event_eventsport_event__sport_type__icontains = data.get('m_op_which'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'esport':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), event_eventesport_event__esport_type__icontains = data.get('m_op_which'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') == 'music':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), event_eventmusic_event__music_type__icontains = data.get('m_op_which'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            elif data.get('type') != 'all':
                try:
                    event = EventModel.objects.filter(event_type__icontains = data.get('type'), privacy__exact = 'public', head__icontains = data.get('m_op_head'))
                except:
                    return HttpResponse('error')
            else:
                event = EventModel.objects.filter(privacy__exact = 'public', head__icontains = data.get('m_op_head'))
            #filter PROVINCE
            if data.get('m_op_place') != '':
                event = event.filter(province__exact = data.get('m_op_place'))
            #filter FEE 
            if data.get('fee') == 'free':
                event = event.filter(fee=0)
            elif data.get('fee') == 'paid':
                event = event.exclude(fee=0)
            else:
                pass
            #filter AGE
            age = data.get('age')
            if age == 'kid':
                event = event.filter(Q(age_begin__gte = 5)&Q(age_begin__lt = 10)|Q(age_end__gte=5)&Q(age_end__lt=10))
            elif age == 'teen':
                event = event.filter(Q(age_begin__gte = 10)&Q(age_begin__lt = 20)|Q(age_end__gte=10)&Q(age_end__lt=20))
            elif age == 'young':
                event = event.filter(Q(age_begin__gte = 20)&Q(age_begin__lt = 30)|Q(age_end__gte=20)&Q(age_end__lt=30))
            elif age == 'aldult':
                event = event.filter(Q(age_begin__gte = 30)&Q(age_begin__lt = 40)|Q(age_end__gte=30)&Q(age_end__lt=40))
            elif age == 'aged':
                event = event.filter(Q(age_begin__gte = 40)&Q(age_begin__lt = 55)|Q(age_end__gte=40)&Q(age_end__lt=55))
            else:
                pass
            #filter QUANTITY
            quantity = data.get('quantity')
            if quantity == 'unlimited':
                event = event.filter(quantity = 0)
            elif quantity == 'limited':
                event = event.exclude(quantity = 0)
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
                event = event.filter((Q(time_begin__gte=beg_time)&Q(time_begin__lte = end_time))|(Q(time_end__gte = beg_time)&Q(time_end__lte = end_time)))
            else:
                event = event.filter(Q(time_begin__lte = now)&Q(time_end__gte = now) | Q(time_begin__gte = now))
            return render(request, 'search/search_event.html', {'events':event, 'head':data.get('m_op_head')})

class Join(Helper):
    def post(self, request):
        try:
            event = EventModel.objects.get(id__exact = int(request.POST.get('event')))
        except Event.DoesNotExist:
            return HttpResponse('error')
        if request.POST.get('action') == 'join':
            try:
                ep = EventParticipants.objects.get(user = request.user , event = event)
                return HttpResponse('error1')
            except EventParticipants.DoesNotExist:
                ep = EventParticipants.objects.create(user = request.user, event = event, accepted = False, guess_invite = True)
                noti = Notification.objects.create(user = event.user, noti_type = 'event-a')
                EventANotification.objects.create(noti = noti, eventparticipants = ep)
                return HttpResponse('ok')
        elif request.POST.get('action') == 'invite':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            try:
                ep = EventParticipants.objects.get(user = user, event = event)
                return HttpResponse('error2')
            except EventParticipants.DoesNotExist:
                ep = EventParticipants.objects.create(user = user, event = event, accepted = False, owner_invite = True)
                noti = Notification.objects.create(user = user, noti_type = 'event-b')
                EventBNotification.objects.create(noti = noti, eventparticipants = ep)
                return HttpResponse('ok')
        elif request.POST.get('action') == 'accept':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error3')
            if request.user == event.user:
                try:
                    ep = EventParticipants.objects.get(event = event, user = user, accepted = False, guess_invite = True)
                    ep.accepted = True
                    ep.save()
                    noti = Notification.objects.create(user = user, noti_type = 'event-e')
                    EventENotification.objects.create(noti = noti, eventparticipants = ep)
                    return HttpResponse('ok')
                except EventParticipants.DoesNotExist:
                    return HttpResponse('error4')
            else:
                try:
                    ep=EventParticipants.objects.get(event = event, user = request.user, accepted = False, owner_invite = True)
                    ep.accepted = True
                    ep.save()
                    noti = Notification.objects.create(user = event.user, noti_type = 'event-f')
                    EventFNotification.objects.create(noti = noti, eventparticipants = ep)
                    return HttpResponse('ok')
                except EventParticipants.DoesNotExist:
                    return HttpResponse('error5')
        elif request.POST.get('action') == 'refuse':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            if event.user == request.user:
                try:
                    ep = EventParticipants.objects.get(user = user, event = event, accepted = False, guess_invite = True)
                    try:
                        zz = EventANotification.objects.get(eventparticipants = ep)
                        zz.noti.delete()
                    except EventANotification.DoesNotExist:
                        pass
                    ep.delete()
                    noti = Notification.objects.create(user = user, noti_type='event-g')
                    EventGNotification.objects.create(event = event, noti = noti)
                    return HttpResponse('ok')
                except EventParticipants.DoesNotExist:
                    return HttpResponse('error')
            else:
                try:
                    ep = EventParticipants.objects.get(user = request.user, event = event, accepted = False, owner_invite = True)
                    try:
                        zz = EventBNotification.objects.get(eventparticipants = ep)
                        zz.noti.delete()
                    except EventBNotification.DoesNotExist:
                        pass
                    ep.delete()
                    noti = Notification.objects.create(user = event.user, noti_type='event-h')
                    EventHNotification.objects.create(event = event, noti = noti,guess=request.user)
                    return HttpResponse('ok')
                except EventParticipants.DoesNotExist:
                    return HttpResponse('error')
        elif request.POST.get('action') == 'decline':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            if event.user == request.user:
                try:
                    ep = EventParticipants.objects.get(user = user, event = event, accepted = False, owner_invite = True)
                    try:
                        zz = EventBNotification.objects.get(eventparticipants = ep)
                        zz.noti.delete()
                    except EventBNotification.DoesNotExist:
                        pass
                    noti = Notification.objects.create(user = user, noti_type = 'event-c')
                    EventCNotification.objects.create(noti = noti, event = event, time_send = ep.time_create)
                    ep.delete()
                    return HttpResponse('ok')
                except EventParticipants.DoesNotExist:
                    return HttpResponse('error')
            else:
                try:
                    ep = EventParticipants.objects.get(user = request.user, event = event, accepted = False, guess_invite = True)
                    try:
                        zz = EventANotification.objects.get(eventparticipants = ep)
                        zz.noti.delete()
                    except EventANotification.DoesNotExist:
                        pass
                    noti = Notification.objects.create(user = event.user, noti_type = 'event-d')
                    EventDNotification.objects.create(noti = noti, event = event, guess=request.user,time_send = ep.time_create)
                    ep.delete()
                    return HttpResponse('ok')
                except EventParticipants.DoesNotExist:
                    return HttpResponse('error')
        elif request.POST.get('action') == 'report':
            try:
                EventReport.objects.create(event = event, user = request.user)
                event.report += 1
                event.save()
                noti = Notification.objects.create(user = event.user, noti_type = 'event-i')
                EventINotification.objects.create(noti = noti, event = event)
                return HttpResponse('ok')
            except IntegrityError:
                return HttpResponse('error')

class SpecificContent(View):
    def get(self, request):
        x = request.GET.get('id')
        event = EventModel.objects.filter(pk = int(x))
        return render(request, 'event/specific_content.html',{'events':event})

class EventPost(View):
    template = 'event/eventstatus_render.min.html'
    def post(self, request):
        try:
            event = EventModel.objects.get(pk__exact = request.POST.get('id'))
        except EventModel.DoesNotExist:
            raise Http404('error')
        ep = event.event_eventparticipants_event.filter(accepted = True)
        if request.user == event.user:
            eventpost = EventPostModel.objects.create(event = event , user =request.user, text = request.POST.get('eve_des'))
            if request.FILES.get('image'):
                eventpost.image = request.FILES.get('image')
                eventpost.save()
            ttt = []
            for i in ep:
                noti = Notification.objects.create(user = i.user, noti_type = 'event-j')
                EventJNotification.objects.create(noti = noti, event=event, user = request.user)
            status = Status.objects.create(status_type = 'eventpost', privacy ='event', eventpost = eventpost, event = event)
            ttt.append(status)
            return render(request, 'status/status.html' ,{'status':ttt})
        else:
            return HttpResponse('error')

class EventPostComment(View):
    template = 'event/eventpostcomment_render.min.html'
    def post(self,request):
        try:
            eventpost = EventPostModel.objects.get(id__exact = request.POST.get('id'))
        except EventPostModel.DoesNotExist:
            return HttpResponse('error')
        eventpostcomment = EventPostCommentModel.objects.create(eventpost = eventpost, user = request.user, comment = request.POST.get('comment'))
        noti = Notification.objects.create(user = eventpost.user ,noti_type = 'event-k')
        EventKNotification.objects.create(noti = noti, eventpostcomment = eventpostcomment)
        return render(request, self.template, {'comment':eventpostcomment})
