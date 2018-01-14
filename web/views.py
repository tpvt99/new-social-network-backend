# response

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseBadRequest
from django.core.urlresolvers import reverse

# class-based views

from django.views.generic import View

# time

from django.utils import timezone
import math
import datetime
import time

# models

from user.models import Info
from page.models import City, Country
from user.models import MyUser
from friend.models import Friend, AddFriend
from group.models import Group

# error
from django.db.utils import IntegrityError

# Create your views here.

class WebPage(View):
    template = 'web/webpagenew.html'
    def get(self, request):
        if request.user.is_authenticated():
            group = Group.objects.filter(group_groupmember_group__user = request.user)
            ref = request.GET.get('ref')
            if ref == None:
                ref = ''
            return render(request , self.template,{'ref':ref,'group':group})
        return HttpResponseRedirect(reverse('frontpage:frontpage'))

class Middle(View):
    template = 'web/middle.html'
    def get(self, request):
        return render(request, self.template )

class Post(View):
    template_act = 'web/act_post.html'
    def get(self, request, *a, **kw):
        return render(request, self.template_act)

class Content(View):
    template = 'web/content.html'
    pass


class RenderParticipate(View):
    template = 'web/participant.html'
    pass

class ErrorPage(View):
    def get(self, request):
        return render(request, 'web/errorpage.html')

class ContactPage(View):
    def get(self, request):
        return render(request, 'web/contactpage.html')

class WebPageNew(View):
    def get(self, request):
        return render(request, 'web/webpagenew.html')

