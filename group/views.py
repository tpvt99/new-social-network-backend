from django.shortcuts import render
from django.views.generic import View

from .models import GroupMember, GroupInvitation
from .models import Group as GroupModel
from .models import GroupPost as GroupPostModel
from status.models import Status
from user.models import MyUser
from .models import GroupMemberDedication

from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import GroupInfo
from friend.models import Friend
from django.db.utils import IntegrityError
from noti.models import Notification, GroupANotification, GroupBNotification, GroupCNotification

# Create your views here.

class Groups(View):
    def get(self, request):
        admin_group = GroupModel.objects.filter(admin = request.user)
        member_group = GroupModel.objects.filter(group_groupmember_group__user = request.user).exclude(admin = request.user)
        return render(request, 'group/groups.html',{'admin_group':admin_group,'member_group':member_group})

class CreateGroup(View):
    def post(self, request):
        name = request.POST.get('group-name')
        privacy = request.POST.get('privacy')
        if name.strip() != '':
            a = GroupModel.objects.create(name = name, privacy = privacy)
            GroupInfo.objects.create(group = a)
            a.admin.add(request.user)
            a.save()
            x = GroupMember.objects.create(user = request.user, group = a, group_type = 'work')
            return HttpResponseRedirect(reverse('group:group', args=(a.id,)))
        else:
            return HttpResponseRedirect(reverse('web:error'))

class Group(View):
    def get(self, request, *a, **kw):
        try:
            idx = kw.get('id')
            try:
                idx = int(idx)
            except ValueError:
                return HttpResponseRedirect(reverse('web:error'))
        except TypeError:
            return HttpResponseRedirect(reverse('web:error'))
        try:
            group = GroupModel.objects.get(pk__exact = idx)
        except GroupModel.DoesNotExist:
            return HttpResponseRedirect(reverse('web:error'))
        member_id = GroupMember.objects.filter(group = group).values_list('user_id', flat = True)
        group_admin_id = group.admin.all().values_list('id', flat = True)
        if request.user.id in group_admin_id:
            is_admin = True
        else:
            is_admin = False
        if request.user.id in member_id:
            is_member = True
        else:
            is_member = False
        status = Status.objects.filter(group = group)
        return render(request, 'group/group.html',{'group':group,'status':status,'is_member':is_member,'is_admin':is_admin})

class GroupPost(View):
    def post(self, request):
        user = request.user
        text = request.POST.get('text')
        image = request.FILES.get('image')
        group_id = request.POST.get('group')
        try:
            group = GroupModel.objects.get(pk__exact = int(group_id))
        except:
            return HttpResponse('error')
        if text.strip() != '':
            a = GroupPostModel.objects.create(user = user, group = group, text = text, image = image)
            s = Status.objects.create(group = group, status_type = 'group-post',privacy = 'group', grouppost = a)
            if image:
                s.has_image = True
                s.save()
            t = []
            t.append(s)
            return render(request,'status/status.html',{'status':t})
        return HttpResponse('error')

class Edit(View):
    def get(self, request):
        which = request.GET.get('which')
        groupid = request.GET.get('group')
        try:
            group = GroupModel.objects.get(id__exact = int(groupid))
        except:
            return HttpResponse('error')
        if which == 'image':
            return render(request, 'group/image_edit.html',{'group':group})
        elif which == 'background':
            return render(request, 'group/background_edit.html',{'group':group})
        elif which == 'intro':
            return render(request, 'group/intro_edit.html',{'group':group})

    def post(self, request):
        groupid = request.POST.get('group')
        which = request.POST.get('which')
        try:
            group = GroupModel.objects.get(id__exact = int(groupid))
        except:
            return HttpResponse('error')
        if request.user in group.admin.all():
            image = request.FILES.get('image')
            if which == 'image':
                try:
                    group.group_groupinfo_group.image = image
                    group.group_groupinfo_group.save()
                except ObjectDoesNotExist:
                    g = GroupInfo.objects.create(group = group)
                    g.image = image
                    g.save()
            elif which == 'background':
                try:
                    group.group_groupinfo_group.background= image
                    group.group_groupinfo_group.save()
                except ObjectDoesNotExist:
                    g = GroupInfo.objects.create(group = group)
                    g.background= image
                    g.save()
            elif which == 'intro':
                intro = request.POST.get('intro')
                try:
                    group.group_groupinfo_group.intro =intro
                    group.group_groupinfo_group.save()
                except ObjectDoesNotExist:
                    g = GroupInfo.objects.create(group = group)
                    g.intro = intro
                    g.save()
            elif which == 'privacy':
                privacy = request.POST.get('privacy')
                if privacy == 'private' or privacy == 'public':
                    group.privacy = privacy
                    group.save()
                    return HttpResponse('ok')
                return HttpResponse('error')
        return HttpResponseRedirect(reverse('group:group', args=(group.id,)))

class Member(View):
    def get(self, request):
        action = request.GET.get('action')
        if action == 'add':
            name = request.GET.get('name')
            groupid = request.GET.get('group')
            try:
                group = GroupModel.objects.get(pk__exact = int(groupid))
            except:
                return HttpResponse('error')
            member_id = GroupInvitation.objects.filter(group = group, is_member = False).values_list('user_id', flat=True)
            friend = Friend.objects.filter(user = request.user, friend__fullname__icontains = name).exclude(friend_id__in = member_id)
            return render(request, 'group/friend_ajax.html',{'friend':friend,'group':group})
    def post(self, request):
        action = request.POST.get('action')
        if action == 'group-type':
            user = request.user
            groupid = request.POST.get('group')
            group_type = request.POST.get('x')
            try:
                group = GroupModel.objects.get(pk__exact = int(groupid))
            except:
                return HttpResponse('error')
            gm = GroupMember.objects.get(user = user, group = group)
            gm.group_type = group_type
            gm.save()
            return HttpResponse('ok')
        elif action == 'follow-edit':
            user = request.user
            groupid = request.POST.get('group')
            try:
                group = GroupModel.objects.get(pk__exact = int(groupid))
            except:
                return HttpResponse('error')
            gm = GroupMember.objects.get(user = user, group = group)
            if gm.follow == True:
                gm.follow = False
            else:
                gm.follow = True
            gm.save()
            return HttpResponse(gm.follow)
        elif action == 'leave':
            user = request.user
            groupid = request.POST.get('group')
            try:
                group = GroupModel.objects.get(pk__exact = int(groupid))
            except:
                return HttpResponse('error')
            if user not in group.admin.all():
                x = GroupMember.objects.get(user = user, group= group)
                x.delete()
                return HttpResponse('ok')
        return HttpResponse('error')

class Join(View):
    def post(self, request):
        try:
            group = GroupModel.objects.get(pk__exact = int(request.POST.get('group')))
        except:
            return HttpResponse('error')
        action = request.POST.get('action')
        if action == 'join':
            try:
                x = GroupInvitation.objects.create(user = request.user, group = group, who_invite = request.user, guess_invite = True)
                for i in group.admin.all():
                    noti = Notification.objects.create(user = i, noti_type = 'group-b')
                    GroupBNotification.objects.create(noti = noti, groupinvitation = x)
                return HttpResponse('ok')
            except IntegrityError:
                return HttpResponse('error')
        elif action == 'accept':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except:
                return HttpResponse('error')
            try:
                x = GroupInvitation.objects.get(user = user, group = group, is_member = False)
                t=GroupMember.objects.create(user = user, group = group, group_type = 'work')
                GroupMemberDedication.objects.create(user = user, group = group, group_member = t)
                x.is_member = True
                x.group_member = t
                x.save()
                if t.guess_invite == True:
                    noti = Notification.objects.create(user = user, noti_type = 'group-c')
                    GroupCNotification.objects.create(noti = noti, group = group)
                return HttpResponse('ok')
            except:
                return HttpResponse('error')
        elif action == 'invite':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except:
                return HttpResponse('error')
            try:
                x = GroupInvitation.objects.create(user = user, who_invite = request.user, owner_invite = True, group = group)
                noti = Notification.objects.create(user = user, noti_type = 'group-a')
                GroupANotification.objects.create(noti = noti, groupinvitation = x)
                return HttpResponse('ok')
            except IntegrityError:
                return HttpResponse('error')
        elif action == 'back':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except:
                return HttpResponse('error')
            try:
                x = GroupInvitation.objects.get(user = user, is_member = False, group = group)
                x.delete()
                return HttpResponse('ok')
            except GroupInvitation.DoesNotExist:
                return HttpResponse('error')
        elif action == 'refuse':
            try:
                user = MyUser.objects.get(pk__exact = int(request.POST.get('who')))
            except:
                return HttpResponse('error')
            try:
                x = GroupInvitation.objects.get(user = user, is_member = False, group = group)
                x.delete()
                return HttpResponse('ok')
            except GroupInvitation.DoesNotExist:
                return HttpResponse('error')
