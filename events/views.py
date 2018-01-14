from django.shortcuts import render
from django.views.generic import View

from event.models import Event
from django.db.models import Q
from status.models import Status
from events.models import EventsPost, EventsPostFriend
from user.models import MyUser
from noti.models import Notification, EventsANotification

# Create your views here.

class Events(View):
    template = 'events/events.html'
    def get(self, request):
        events = Event.objects.filter(Q(event_eventparticipants_event__accepted = True) & Q(event_eventparticipants_event__user = request.user)).order_by('-time_create')
        return render(request, self.template, {'events':events})

class Create(View):
    template = 'status/status.html'
    def post(self, request):
        data = request.POST
        try:
            x = int(request.POST.get('act_id'))
        except:
            return HttpResponse('error')
        event = Event.objects.get(pk__exact = x)
        if data.get('des').strip() != '':
            eventspost = EventsPost.objects.create(user= request.user, event =event , text = data.get('des'), privacy = request.POST.get('privacy'))
        else:
            return HttpResponse('error')
        if request.FILES.get('image'):
            eventspost.image = request.FILES.get('image')
            eventspost.save()
        fr_id = data.getlist('hiddenfr')
        if fr_id:
            for i in fr_id:
                t = MyUser.objects.get(pk__exact = int(i))
                EventsPostFriend.objects.create(eventspost =eventspost , friend = t)
                noti = Notification.objects.create(user = t, noti_type = 'events-a')
                EventsANotification.objects.create(noti = noti, event = event , eventspost = eventspost )
        status = Status.objects.create(status_type = 'eventspost', privacy = eventspost.privacy, eventspost=eventspost , user = request.user)
        t=[]
        t.append(status)
        return render(request, self.template , {'status':t})
