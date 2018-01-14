from django.db import models
from user.models import User
from files.models import Image
import uuid

# Create your models here.

class NewFeed(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    isMinimizedFeed = models.BooleanField(default = False)

class OnlineTime(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)


class FollowTimeline(models.Model):
    # name of timeline ex family, friends, work, school
    name = models.CharField(max_length = 1000)
    # id for each above name
    follow_id = models.IntegerField(unique = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    members = models.ManyToManyField(User, related_name = "%(app_label)s_%(class)s_members")
