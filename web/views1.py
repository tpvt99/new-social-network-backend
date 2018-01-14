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

# models

from user.models import Info
from page.models import City, Country
from user.models import MyUser
from friend.models import Friend, AddFriend
from vote.models import ActivityVote

# error
from django.db.utils import IntegrityError

# Create your views here.

class WebPage(View):
    template = 'web/webpage.html'
    def get(self, request):
        if request.user.is_authenticated():
            return render(request , self.template)
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
    def get(self, request, *a, **kw):
        try:
            page = int(request.GET.get('page'))
            id_post = int(request.GET.get('id'))
        except TypeError:
            raise Http404('error')
        under_limit = 0
        i = 1
        while i < page:
            under_limit += 5
            i+=1
        my_acts = list(Activity.objects.filter(user=request.user).order_by('-create_date'))
        fr = Friend.objects.filter(user = request.user)
        fr_list = list()
        for x in fr:
            fr_list.append(x.friend)
        your_acts = list(Activity.objects.filter(user__in = fr_list).order_by("-create_date"))
        acts = your_acts + my_acts
        acts.sort(key = lambda x : x.create_date, reverse = True)
        acts = acts[under_limit:under_limit + 5]
        try:
            act = acts[id_post]
            try:
                participants = act.activityparticipants.participants.all().exclude(id = act.user.id)
            except:
                participants = []
            comments = act.activitycomment_set.all()
            ai = ActivityImage.objects.filter(activity = act, is_temporary = False)
            votes = act.activityvote_set.all()
            if votes:
                try:
                    vote_1 = ActivityVote.objects.get(activity = act, user = request.user)
                except ActivityVote.DoesNotExist:
                    vote_1 = ''
            else:
                vote_1 = ''
        except IndexError:
            return HttpResponse('error')
        ap = ActivityParticipants.objects.get(activity = act)
        ownerinfo = MoreInfo.objects.get(person = act.user, activityparticipants = ap)
        timedel = datetime.timedelta(hours = act.timezone)
        post_time = act.create_date + timedel
        timedelta = timezone.now() - act.create_date
        act_se = ActivitySeries.objects.filter(activity = act).order_by('time')
        return render(request, self.template, {'act':act, 'participants':participants,'comments':comments,'votes':votes,'vote_1':vote_1,'ownerinfo':ownerinfo, 'actimgs':ai, 'post_time':post_time, 'act_se':act_se, 'timedelta':timedelta})


class RenderParticipate(View):
    template = 'web/participant.html'
    def get(self, request):
        try:
            parid = int(request.GET.get('p'))
            actid = int(request.GET.get('a'))
        except ValueError:
            raise Http404('error')
        who_vote = MyUser.objects.get(id = request.user.id)
        who_being_vote = MyUser.objects.get(pk = parid)
        activity = Activity.objects.get(pk = actid)

        friends_of_being_vote = Friend.objects.filter(user = who_being_vote) # friends of being vote to count total percent
        friends_of_mine = Friend.objects.filter(user = who_vote)

        friend_list_being = list()
        friend_list_mine = list()
        for x in friends_of_being_vote:
            friend_list_being.append(x.friend)

        for x in friends_of_mine:
            friend_list_mine.append(x.friend)

        ap = ActivityParticipants.objects.get(activity = activity)
        ap_pp = ap.participants.all()
        if who_being_vote in friend_list_mine or who_being_vote == who_vote: # allow vote only if is my friend and myself
            if who_vote in ap_pp and who_being_vote in ap_pp: # check if hacker change id of friends but not in activity participants or friend share friends but not ivite you
                moreinfo = MoreInfo.objects.get(person = who_being_vote, activityparticipants = ap)
                try:
                    vote = Vote.objects.get(info = moreinfo, who_being_vote = who_being_vote , who_vote = who_vote)
                    # count vote
                    votes = Vote.objects.filter(info = moreinfo, who_being_vote = who_being_vote)
                    count_vote = 0
                    total_vote = 1
                    for zzz in votes:
                        if zzz.been_vote == True:
                            count_vote += 1
                    
                    for ttt in friend_list_being:
                        if ttt in ap_pp:
                            total_vote += 1
                    percent = math.ceil((count_vote/total_vote)*100)
                    # done count
                    is_vote = vote.been_vote
                    return render(request, self.template, {'participant':who_being_vote,'act':activity,'been_vote':is_vote, 'percent':str(percent)+'%','is_friend':True,'mf':moreinfo})
                except Vote.DoesNotExist:
                    votes = Vote.objects.filter(info = moreinfo, who_being_vote = who_being_vote)
                    count_vote = 0
                    total_vote = 1
                    for zzz in votes:
                        if zzz.been_vote == True:
                            count_vote += 1
                    
                    for ttt in friend_list_being:
                        if ttt in ap_pp:
                            total_vote += 1
                    percent = math.ceil((count_vote/total_vote)*100)
                    return render(request, self.template, {'participant':who_being_vote,'act':activity,'been_vote':False, 'percent':str(percent)+'%', 'is_friend':True,'mf':moreinfo})
            elif who_vote not in ap_pp: # you are not invited
                moreinfo = MoreInfo.objects.get(person = who_being_vote, activityparticipants = ap)
                votes = Vote.objects.filter(info = moreinfo, who_being_vote = who_being_vote)
                count_vote = 0
                total_vote = 1
                for zzz in votes:
                    if zzz.been_vote == True:
                        count_vote += 1
                
                for ttt in friend_list_being:
                    if ttt in ap_pp:
                        total_vote += 1
                percent = math.ceil((count_vote/total_vote)*100)
                return render(request, self.template, {'participant':who_being_vote,'act':activity,'been_vote':False, 'percent':str(percent)+'%', 'is_friend':False,'mf':moreinfo})
            else:
                return HttpResponse('error hacker')
        else:
            moreinfo = MoreInfo.objects.get(person = who_being_vote, activityparticipants = ap)
            votes = Vote.objects.filter(info = moreinfo, who_being_vote = who_being_vote)
            count_vote = 0
            total_vote = 1
            for zzz in votes:
                if zzz.been_vote == True:
                    count_vote += 1
            
            for ttt in friend_list_being:
                if ttt in ap_pp:
                    total_vote += 1
            percent = math.ceil((count_vote/total_vote)*100)
            return render(request, self.template, {'participant':who_being_vote,'act':activity,'been_vote':False, 'percent':str(percent)+'%', 'is_friend':False,'mf':moreinfo})


