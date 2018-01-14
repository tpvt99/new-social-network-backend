from .models import Post
from user.serialize import serialize_user_basic
from files.serialize import serialize_image
from django.core.exceptions import ObjectDoesNotExist

def serialize_friendtag(post):
    data = []
    try:
        ft = post.post_postfriendtag_post
        f = ft.friend.all()
        for i in f:
            data.append(serialize_user_basic(i))
        return data
    except ObjectDoesNotExist:
        return data

def serialize_post(post):
    images = []
    if post.has_link_image:
        image_objects = post.image.all()
        for i in image_objects:
            images.append(serialize_image(i))
    return {
    'user': serialize_user_basic(post.user),
    'text': post.text,
    'saleItem': post.sale_item,
    'time': post.time_create.isoformat(),
    'has_link_image': post.has_link_image,
    'old_image': post.old_image.url if post.old_image else '',
    'images': images,
    'friends': serialize_friendtag(post)
    }
