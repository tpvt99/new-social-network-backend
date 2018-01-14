from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import View
from .models import Trait
from status.models import Status
from user.models import MyUser
from friend.models import FriendHeart, FriendRelationship, Friend

from noti.models import Notification, TraitANotification

# Create your views here.

class AddTraitAjax(View):
    def get(self, request):
        return render(request, 'trait/addtraitajax.html')

class Create(View):
    def post(self, request):
        user_send = request.user
        try:
            user_receive_id = request.POST.get('hiddenfr-t')
            try:
                user_receive_id = int(user_receive_id)
                try:
                    user_receive = MyUser.objects.get(id__exact = user_receive_id)
                except MyUser.DoesNotExist:
                    return HttpResponseRedirect(reverse('web:error'))
            except ValueError:  #ValueError when data is not an integer
                return HttpResponseRedirect(reverse('web:error'))
        except TypeError:  #TypeError when None data
            return HttpResponseRedirect(reverse('web:error'))
        trait_type = request.POST.get('trait_type')
        trait_des = request.POST.get('trait-des')
        trait_file = request.FILES.get('file')
        if trait_type.strip() and trait_des.strip() and trait_file:
            t = Trait.objects.create(user_send = request.user, user_receive = user_receive, trait_type = trait_type, text = trait_des,image=trait_file)
            status = Status.objects.create(user = user_receive, status_type="create-trait", trait = t, privacy="public")
            noti = Notification.objects.create(user = user_receive, noti_type='trait-a')
            TraitANotification.objects.create(noti = noti, trait = t)
        if status.user:
            try:
                user = request.user
                friend = status.user
                x = Friend.objects.get(user = user, friend = friend)
                try:
                    tt = FriendRelationship.objects.get(user = request.user, friend = x)
                except FriendRelationship.DoesNotExist:
                     tt = FriendRelationship.objects.create(user = request.user, friend = x)
                finally:
                        a = FriendHeart.objects.create(user = user, friend = friend, friendrelationship = tt, source = 'trait',reason = 'trait',trait = t)
                        a.heart = 10
                        tt.friend_heart += a.heart
                        a.save()
                        tt.save()
            except Friend.DoesNotExist:
                pass
        return HttpResponseRedirect(reverse('web:webpage'))
