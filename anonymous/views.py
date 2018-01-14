from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Post
from .models import Comment as CommentModal
from .models import Vote as VoteModel
from django.db.utils import IntegrityError
from friend.models import Friend
import time
from django.core.urlresolvers import reverse
from django.db.models import Q
from noti.models import AnonymousANotification, AnonymousBNotification, Notification
from friend.models import Friend

# Create your views here.

from django.views.generic import View

class Home(View):
    template = 'anonymous/home.html'
    def get(self, request):
        if request.user.is_authenticated():
            t = Friend.objects.filter(user = request.user)
            if len(t) > 10:
                return render(request, self.template)
            return HttpResponseRedirect(reverse('web:webpage'))
        else:
            return HttpResponseRedirect(reverse('frontpage:frontpage'))

class Content(View):
    template = 'anonymous/status_min.html'
    def get(self, request):
        try:
            page = int(request.GET.get('page'))
        except:
            return HttpResponse('error')
        fr_list = Friend.objects.filter(user = request.user).values_list('friend_id', flat = True)
        status = Post.objects.filter(Q(user = request.user)|Q(user_id__in = list(fr_list))).order_by('-time')[page*10:page*10+10]
        return render(request, self.template, {'status':status})

class Status(View):
    template = 'anonymous/content.html'
    def post(self, request):
        des = request.POST.get('des')
        user_des = request.POST.get('user')
        if len(user_des) > 25:
            return HttpResponse('error')
        post = Post.objects.create(user = request.user, des = des, user_des = user_des)
        return render(request, self.template, {'stat':post})

class Comment(View):
    template = 'anonymous/comment.html'
    def post(self, request):
        if request.is_ajax():
            if request.POST.get('ano') == 'false':
                ano = False
            else:
                ano = True
            post = Post.objects.get(pk__exact = int(request.POST.get('stat')))
            comment = CommentModal.objects.create(post = post, user = request.user, des = request.POST.get('des') ,is_anonymous = ano, user_des = '')
            if request.user != post.user:
                noti = Notification.objects.create(user = post.user, noti_type = 'anonymous-b')
                AnonymousBNotification.objects.create(noti = noti, ano_post = post, comment = comment)
            return render(request, self.template, {'comment':comment})

class Vote(View):
    def post(self, request):
        post = Post.objects.get(pk__exact = request.POST.get('id'))
        try:
            vote = VoteModel.objects.create(user = request.user, post = post, been_vote = True)
            post.heart += 1
            post.save()
            if request.user != post.user:
                noti = Notification.objects.create(user = post.user, noti_type = 'anonymous-a')
                AnonymousANotification.objects.create(noti = noti, ano_post = post, vote = vote)
            response = JsonResponse({'a':'ok','vote':post.heart})
        except IntegrityError:
            vote = VoteModel.objects.get(user = request.user, post = post)
            if vote.been_vote == True:
                vote.been_vote = False
                vote.save()
                post.heart -= 1
                post.save()
                response = JsonResponse({'a':'no','vote':post.heart})
            else:
                vote.been_vote = True
                vote.save()
                post.heart += 1
                post.save()
                response = JsonResponse({'a':'ok','vote':post.heart})
        return HttpResponse(response)

class SpecificContent(View):
    template = 'anonymous/specific_content.html'
    def get(self,request):
        x = int(request.GET.get('id'))
        ano = Post.objects.filter(pk__exact = x)
        return render(request, self.template,{'status':ano})
