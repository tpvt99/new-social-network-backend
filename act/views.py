from django.shortcuts import render
from django.views.generic import View
import ast
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from friend.models import Friend
from .models import Act, ActFriend, ActPostTagFriend
from .models import ActPost as ActPostModel
from user.models import MyUser
from status.models import Status
from post.models import Post as PostModel
from noti.models import Notification, ActANotification, ActBNotification

# Create your views here.

class Activity(View):
    template = 'act/act.html'
    def get(self, request, *a, **kw):
        try:
            t = int(kw.get('id'))
        except:
            return HttpResponseRedirect(reverse('web:webpage'))
        act = Act.objects.get(pk__exact = t)
        actpost = act.actpost_set.all()
        x = []
        for i in actpost:
            x.append(i.status_set.all()[0])
        fr = ActFriend.objects.filter(act = act).values_list('friend_id',flat=True)
        if request.user == act.user or request.user.id in fr:
            return render(request, self.template, {'status':x,'act':act})
        else:
            return HttpResponseRedirect(reverse('web:webpage'))

class FriendAjax(View):
    template = 'act/friendajax.html'
    def get(self, request):
        key = request.GET.get('key')
        ex = request.GET.get('except')
        if ex:
            ex = ast.literal_eval(ex)
        if key:
            if ex:
                friends = Friend.objects.filter(user = request.user, friend__fullname__icontains = key).exclude(friend_id__in = ex)
            else:
                friends = Friend.objects.filter(user = request.user, friend__fullname__icontains = key)
        else:
            friends = None
        return render(request, self.template, {'friends':friends})

class Create(View):
    def post(self,request):
        data = request.POST
        if data.get('actin').strip() != '' or data.get('desin').strip() != '':
            act = Act.objects.create(user = request.user, head = data.get('actin'), des = data.get('desin'))
        else:
            return HttpResponse('error')
        act.province = data.get('province')
        act.province_unicode = data.get('hiddenprovince')
        act.image = request.FILES.get('act-image')
        act.privacy = data.get('privacy')
        act.save()
        # for friend
        fr_id = data.getlist('hiddenfr')
        if fr_id:
            for i in fr_id:
                t = MyUser.objects.get(pk__exact = int(i))
                ActFriend.objects.create(act = act, friend = t, accepted = False)
                noti = Notification.objects.create(user = t, noti_type = 'act-a')
                ActANotification.objects.create(noti = noti, act = act)
        status = Status.objects.create(status_type = 'act', privacy = act.privacy, act = act, user = request.user)
        t = []
        t.append(status)
        return render(request, 'status/status.html',{'status':t})

class ActPost(View):
    def post(self, request):
        data = request.POST
        try:
            x = int(request.POST.get('act_id'))
        except:
            return HttpResponse('error')
        act = Act.objects.get(pk__exact = x)
        fr = ActFriend.objects.filter(act = act).values_list('friend_id',flat=True)
        if data.get('des').strip() != '':
            if act.user == request.user or request.user.id in fr:
                actpost = ActPostModel.objects.create(user= request.user, act = act, des = data.get('des'), privacy = request.POST.get('privacy'))
            else:
                return HttpResponse('error')
        else:
            return HttpResponse('error')
        if request.FILES.get('image'):
            actpost.image = request.FILES.get('image')
            actpost.save()
        fr_id = data.getlist('hiddenfr')
        if fr_id:
            for i in fr_id:
                t = MyUser.objects.get(pk__exact = int(i))
                ActPostTagFriend.objects.create(actpost = actpost, friend = t)
                noti = Notification.objects.create(user = t, noti_type = 'act-b')
                ActBNotification.objects.create(noti = noti, actpost = actpost)
        status = Status.objects.create(status_type = 'actpost', privacy = actpost.privacy, actpost = actpost, user = request.user)
        t=[]
        t.append(status)
        return render(request, 'status/status.html', {'status':t})

class UpdateImage(View):
    def post(self,request):
        try:
            act_id = int(request.POST.get('act'))
        except:
            return HttpResponseRedirect(reverse('life:lifepage'))
        act = Act.objects.get(id__exact = act_id)
        image =request.POST.get('image')
        if image:
            act.image = image
            act.save()
        return HttpResponseRedirect(reverse('life:lifepage'))
