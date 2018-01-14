from django.db import models
from django.conf import settings
from user.models import User
from files.models import Image

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add = True)
    old_image = models.ImageField(upload_to = 'media', null = True)

    # new link image
    has_link_image = models.BooleanField(default = False)
    image = models.ManyToManyField(Image, related_name = "%(app_label)s_%(class)s_image")

    # this is for sales
    sale_item = models.CharField(max_length = 100, null = True)

class PostFriendTag(models.Model):
    post = models.OneToOneField(Post, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_post")
    friend = models.ManyToManyField(User, related_name = "%(app_label)s_%(class)s_friend")
