from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from security.response import set_response_header
from .models import Post as PostModel
from status.serialize import status_serialize
from authentication.auth import check_authentication
from user.method import get_user
from status.models import Status, StatusReaction
from files.models import Image as ImageModel
from .models import PostFriendTag
from user.models import User
from noti.models import Notification, PostANotification

# Create your views here.

class Create(View):
    def post(self, request):
        if check_authentication(request, True):
            user = get_user(request)
            data = request.POST
            post = PostModel.objects.create(user = user, text = data.get('textarea'))
            # sale items 
            post.sale_item = data.get('saleItem')
            post.save()
            # for friend
            fr_id = data.getlist('friendIds')
            if fr_id:
                pf = PostFriendTag.objects.create(post = post)
                for i in fr_id:
                    t = User.objects.get(user_id = i)
                    pf.friend.add(t)
                    noti = Notification.objects.create(user = t, noti_type = 'post-a')
                    PostANotification.objects.create(noti = noti, post = post)
            # for images
            images_id = data.getlist('images_id')
            for i in images_id:
                img = ImageModel.objects.get(pk = int(i))
                img.image_type = 'post-newfeed'
                img.user = user
                img.has_saved = True
                img.save()
                post.has_link_image = True
                post.image.add(img)
                post.save()
            status = Status.objects.create(verb = 'post', privacy = 'friend', post = post, user = user)
            if request.POST.get('verb') == 'sale':
                status.verb = 'sale'
                status.save()

            #for reactions
            use_default_reaction = True
            use_custom_reaction = False
            reaction = data.get('reaction')
            if reaction.strip() and len(reaction.strip()) < 30:
                use_default_reaction = False
                use_custom_reaction = True
                status.use_default_reaction = use_default_reaction
                status.use_custom_reaction = use_custom_reaction
                status.save()
                sr = StatusReaction.objects.create(status = status, reactionName = reaction, reactionType = 'a')
            else:
                sr = StatusReaction.objects.create(status = status, reactionName = 'like', reactionType = '1', icon = 'heart', vote = 0)
            response = JsonResponse({'data': status_serialize(status, user), 'status_code':'ok'})
            set_response_header(response)
            return response
        else:
            response = JsonResponse({'status_code':'error'})
            set_response_header(response)
            return response
