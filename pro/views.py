from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic import View
from django.db.models import Q
import pprint
import json
import time
import datetime

# models

from user.models import Info,MyUser, BornPlace, LivePlace, InfoWork, InfoEducationSchool, InfoEducationUniversity
from user.models import User
from friend.models import Friend
from activities.models import Activity
from plan.models import Plan
from status.models import Status
from django.db.models import Q

from user.serialize import serialize_user_basic
from user.method import get_user
from security.response import set_response_header
from authentication.auth import check_authentication
from .serialize import basic_info

# Create your views here.


class Profile(View):
    def get(self, request, *a, **kw):
        isSelf = False
        isStranger = False
        isFriend = False
        user = None
        if check_authentication(request):
            user = get_user(request)
            friends = Friend.objects.filter(user = user)
        profile_url = request.GET.get('profileUrl')
        try:
            user_visited = User.objects.get(account__profilename__exact = profile_url)
        except User.DoesNotExist:
            response = JsonResponse({'status_code': 'error'})
            set_response_header(response)
            return response
        if user:
            if user == user_visited:
                isSelf = True
            elif user_visited.id in friends.values_list('friend_id', flat = True):
                isFriend = True
            else:
                isStranger = True
        data = {
            'user': serialize_user_basic(user_visited),
            'relationShip': {
                'isSelf': isSelf,
                'isFriend': isFriend,
                'isStranger': isStranger
            },
            'status_code': 'ok'
        }
        response = JsonResponse(data)
        set_response_header(response)
        return response

class BasicInfo(View):
    def get(self, request):
        user_id = request.GET.get('id')
        try:
            user = User.objects.get(user_id__exact = user_id)
        except User.DoesNotExist:
            response = JsonResponse({'status_code':'error'})
            set_response_header(response)
            return response
        data = {
            'data': basic_info(user),
            'status_code': 'ok'
        }
        response = JsonResponse(data)
        set_response_header(response)
        return response

class ChangeProfilePic(View):
    def get(self, request):
        return render(request, 'pro/profile_pic.html')
    def post(self, request):
        img = request.FILES.get('profile_pic')
        info = Info.objects.get(user = request.user)
        info.profile_pic = img
        info.save()
        Status.objects.create(user = request.user,status_type="change-profilepic", privacy="public")
        return HttpResponseRedirect(reverse('pro:profile'))

class ChangeBackgroundPic(View):
    def get(self, request):
        return render(request, 'pro/background_pic.html')
    def post(self, request):
        img = request.FILES.get('background_pic')
        info = Info.objects.get(user = request.user)
        info.background_pic = img
        info.save()
        return HttpResponseRedirect(reverse('pro:profile'))



class AddEditPlace(View):
    template_born = 'pro/addeditborn_ajax.html'
    template_live = 'pro/addeditlive_ajax.html'
    def get(self, request, *a, **kw):
        if request.is_ajax():
            if kw.get('type') == 'born':
                bornplace = BornPlace.objects.filter(user = request.user)
                return render(request, self.template_born, {'bornplace':bornplace})
            elif kw.get('type') == 'live':
                liveplace = LivePlace.objects.filter(user = request.user)
                return render(request, self.template_live, {'liveplace':liveplace})

    def post(self, request, *a, **kw):
        if kw.get('type') == 'born':
            place = request.POST.get('born-place')
            privacy = request.POST.get('share')
            try:
                b = BornPlace.objects.get(user = request.user)
                if place.strip() == '':
                    b.delete()
                else:
                    b.place = place
                    if privacy:
                        b.privacy = privacy
                    else:
                        b.privacy = 'public'
                    b.save()
            except BornPlace.DoesNotExist:
                if place.strip() == '':
                    pass
                else:
                    b = BornPlace.objects.create(user = request.user, place = place)
                    if privacy:
                        b.privacy = privacy
                    else:
                        b.privacy = 'public'
                    b.save()
            return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')
        elif kw.get('type') == 'live':
            place = request.POST.get('live-place')
            privacy = request.POST.get('share')
            try:
                b = LivePlace.objects.get(user = request.user)
                if place.strip() == '':
                    b.delete()
                else:
                    b.place = place
                    if privacy:
                        b.privacy = privacy
                    else:
                        b.privacy = 'public'
                    b.save()
            except LivePlace.DoesNotExist:
                if place.strip() == '':
                    pass
                else:
                    b = LivePlace.objects.create(user = request.user, place = place)
                    if privacy:
                        b.privacy = privacy
                    else:
                        b.privacy = 'public'
                    b.save()
            return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')

class AddEditWork(View):
    template = 'pro/addeditwork_ajax.html'
    template2 = 'pro/addeditwork_ajax.html'
    def get(self, request, *a, **kw):
        t = kw.get('type')
        if t == 'add':
            return render(request, self.template)
        elif t == 'edit':
            work = InfoWork.objects.get(pk__exact = int(request.GET.get('id')))
            return render(request, self.template2, {'work':work})

    def post(self, request, *a, **kw):
        t = kw.get('type')
        if t == 'add':
            company = request.POST.get('company')
            if company.strip() != '':
                position = request.POST.get('position')
                privacy = request.POST.get('privacy')
                begin_year = request.POST.get('begin_year')
                begin_time = datetime.date(year = int(begin_year), month=1,day=1)
                end_year = request.POST.get('end_year')
                end_time = datetime.date(year = int(end_year), month=1,day=1)
                if int(end_year) >= int(begin_year):
                    InfoWork.objects.create(user = request.user, company = company, position = position, time_begin = begin_time, time_end = end_time ,privacy = privacy)
            return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')
        elif t == 'edit':
            work = InfoWork.objects.get(pk = request.POST.get('work'))
            company = request.POST.get('company')
            if company.strip() != '':
                work.company = company
                work.position = request.POST.get('position')
                work.privacy = request.POST.get('privacy')
                begin_year = request.POST.get('begin_year')
                begin_time = datetime.date(year = int(begin_year), month=1,day=1)
                end_year = request.POST.get('end_year')
                end_time = datetime.date(year = int(end_year), month=1,day=1)
                if int(end_year) >= int(begin_year):
                    work.time_end = end_time
                    work.time_begin = begin_time
                work.save()
            else:
                work.delete()
            return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')

class AddEditEducation(View):
    template_uni = 'pro/addedituni_ajax.html'
    template_sch = 'pro/addeditsch_ajax.html'
    def get(self, request, *a, **kw):
        typex = kw.get('type')
        kind = kw.get('kind')
        if typex == 'uni':
            if kind == 'add':
                return render(request, self.template_uni)
            else:
                edu = InfoEducationUniversity.objects.get(id__exact = int(request.GET.get('id')))
                return render(request, self.template_uni,{'edu':edu})
        else:
            if kind == 'add':
                return render(request, self.template_sch)
            else:
                edu = InfoEducationSchool.objects.get(id__exact = int(request.GET.get('id')))
                return render(request, self.template_sch, {'edu':edu})

    def post(self, request, *a, **kw):
        typex = kw.get('type')
        kind = kw.get('kind')
        if typex == 'sch':
            if kind == 'add':
                school = request.POST.get('school')
                privacy = request.POST.get('privacy')
                begin_year = int(request.POST.get('begin_year'))
                end_year = int(request.POST.get('end_year'))
                begin_time = datetime.date(year = begin_year, month = 1, day=1)
                end_time = datetime.date(year = end_year, month =1, day = 1)
                if school.strip() != '':
                    s = InfoEducationSchool.objects.create(user = request.user, school = school, time_begin = begin_time, time_end = end_time, privacy = privacy)
                return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')
            else:
                edu = InfoEducationSchool.objects.get(id__exact = int(request.POST.get('edu')))
                school = request.POST.get('school')
                privacy = request.POST.get('privacy')
                begin_year = int(request.POST.get('begin_year'))
                end_year = int(request.POST.get('end_year'))
                begin_time = datetime.date(year = begin_year, month = 1, day=1)
                end_time = datetime.date(year = end_year, month =1, day = 1)
                if school.strip() != '':
                    edu.school = school;
                    edu.privacy = privacy
                    edu.time_begin = begin_time
                    edu.time_end = end_time
                    edu.save()
                else:
                    edu.delete()
                return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')
        elif typex == 'uni':
            if kind == 'add':
                university = request.POST.get('university')
                major = request.POST.get('major')
                privacy = request.POST.get('privacy')
                begin_year = int(request.POST.get('begin_year'))
                end_year = int(request.POST.get('end_year'))
                begin_time = datetime.date(year = begin_year, month = 1, day=1)
                end_time = datetime.date(year = end_year, month =1, day = 1)
                if university.strip() != '':
                    InfoEducationUniversity.objects.create(user = request.user, university = university, major = major, privacy = privacy, time_begin = begin_time, time_end = end_time)
                return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')
            elif kind == 'edit':
                edu = InfoEducationUniversity.objects.get(pk__exact = request.POST.get('edu'))
                university = request.POST.get('university')
                major = request.POST.get('major')
                privacy = request.POST.get('privacy')
                begin_year = int(request.POST.get('begin_year'))
                end_year = int(request.POST.get('end_year'))
                begin_time = datetime.date(year = begin_year, month = 1, day=1)
                end_time = datetime.date(year = end_year, month =1, day = 1)
                if university.strip() != '':
                    edu.university = university
                    edu.major = major
                    edu.privacy = privacy
                    edu.time_begin = begin_time
                    edu.time_end = end_time
                    edu.save()
                else:
                    edu.delete()
                return HttpResponseRedirect('/profile/?id='+str(request.user.id)+'&w=info')

class Head(View):
    template = 'pro/profile_head.html' 
    def get(self, request):
        info = Info.objects.get(user = request.user)
        return render(request, self.template, {'info':info})
    def post(self, request):
        head = request.POST.get('head')
        info = Info.objects.get(user = request.user)
        info.head = head
        info.save()
        return HttpResponseRedirect('/profile/')

class Bio(View):
    template = 'pro/profile_bio.html' 
    def get(self, request):
        if request.GET.get('a') == 'add':
            return render(request, self.template)
        else:
            info = Info.objects.get(user = request.user)
            return render(request, self.template, {'info':info})
    def post(self, request):
        bio = request.POST.get('bio')
        info = Info.objects.get(user = request.user)
        info.bio=bio 
        info.save()
        return HttpResponseRedirect('/profile/')

class Name(View):
    template = 'pro/profile_name.html'
    def get(self, request):
        return render(request, self.template)
    def post(self, request):
        try:
            firstname =request.POST.get('f-firstname').strip()
            lastname = request.POST.get('f-lastname').strip()
        except:
            return HttpResponseRedirect('/profile/')
        if firstname and lastname:
            user = MyUser.objects.get(pk__exact = int(request.user.id))
            user.fullname = firstname + ' '+ lastname
            user.save()
            user.info.firstname = firstname
            user.info.lastname = lastname
            user.info.save()
        return HttpResponseRedirect('/profile/')


class Content(View):
    def get(self, request):
        try:
            page = int(request.GET.get('page'))
        except:
            return HttpResponse('error')
        try:
            t = int(request.GET.get('id'))
            owner_user = MyUser.objects.get(pk__exact = t)
        except:
            owner_user = request.user
        if request.user == owner_user:
            status  = Status.objects.filter(user = request.user).order_by('-time_create')[page*10:page*10+10]
            return render(request, 'status/status.html' ,{'status':status})
        else:
            t = Friend.objects.filter(user = owner_user)
            for i in t:
                if request.user == i.friend:
                    status = Status.objects.filter(Q(user = owner_user), Q(privacy = 'public') | Q(privacy = 'friend')).order_by('-time_create')[page*10:page*10+10]
                    return render(request, 'status/status.html' ,{'status':status})
            status = Status.objects.filter(user = owner_user, privacy = 'public').order_by('-time_create')[page*10:page*10+10]
            return render(request, 'status/status.html', {'status':status})
