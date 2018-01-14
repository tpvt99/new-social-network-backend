from django.shortcuts import render
from django.views.generic import View
import imghdr
from django.http import HttpResponse, HttpResponseRedirect
from friend.models import Friend
from django.db.models import Q
from .models import Moment as MomentModel
from django.core.urlresolvers import reverse
from .models import MomentComment as MomentCommentModel
from plustag.models import PlustagLife
from django.db.utils import IntegrityError
import re
from plustag.models import plus_tag

# Create your views here.

class Moment(View):
    def get(self, request):
        fr = Friend.objects.filter(user = request.user).values_list('friend_id', flat=True)
        images = MomentModel.objects.filter(Q(user = request.user) | Q(user_id__in = list(fr))).order_by('-time_create')
        return render(request, 'moment/home.html', {'images':images})

class Create(View):
    def post(self, request):
        text = request.POST.get('text')
        image = request.FILES.get('image')
        if image != None and len(text) < 100:
            x = imghdr.what(image)
            if x == 'jpeg' or x == 'png' or x =='jpg':
                MomentModel.objects.create(user = request.user, text = text, image = image, privacy = "public")
        return HttpResponseRedirect(reverse('moment:moment'))

class Comment(View):
    def define_plustag_image(self,moment, user_send_plus, comment):
        #if moment.user != user_send_plus: we want you to have plustag too
        re_exp = re.compile(r'^\+[a-z]+| \+[a-z]+')
        re_result = list(set(re_exp.findall(comment)))
        for i in re_result:
            if i.strip() in plus_tag:
                try:
                    PlustagLife.objects.create(user_receive_plus = moment.user, user_send_plus = user_send_plus, moment = moment, plustag_type = i.strip())
                except IntegrityError:
                    pass

    def post(self, request):
        text = request.POST.get('text')
        user = request.user
        moment_id = request.POST.get('m')
        try:
            moment_id = int(moment_id)
            moment = MomentModel.objects.get(pk__exact = moment_id)
        except:
            return HttpResponse('error')
        if text != None and text.strip() != '':
            self.define_plustag_image(moment = moment, user_send_plus = user, comment = text)
            c = MomentCommentModel.objects.create(user = request.user, moment = moment, comment = text)
            t = []
            t.append(c)
            return render(request, 'moment/comment.html', {'comments':t})
