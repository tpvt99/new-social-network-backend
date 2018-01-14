from django.db import models
from django.conf import settings
from status.models import Status
from trait.models import Trait
from user.models import User

# Create your models here.

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
    friend_since = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user','friend')

class AddFriend(models.Model):
    inviter = models.ForeignKey(User, on_delete = models.CASCADE,related_name = "%(app_label)s_%(class)s_inviter")
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_receiver")
    invite_time = models.DateTimeField(auto_now_add = True)
    is_friend = models.BooleanField(default = False)
    read = models.BooleanField(default = False)

    class Meta:
        unique_together = ("inviter", "receiver")

class FriendRelationship(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    friend = models.OneToOneField(Friend, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_friend")
    friend_heart = models.IntegerField(default = 0)
    
class FriendHeart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
    friendrelationship = models.ForeignKey(FriendRelationship, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_friendrelationship")
    source = models.CharField(max_length = 100)
    reason = models.CharField(max_length = 100, null = True)
    heart = models.IntegerField(default = 0)
    time_create = models.DateTimeField(auto_now_add = True)
    time_modify = models.DateTimeField(auto_now = True)
    #like,comment and share of status, trait and challenge friend, tagging friend in picture
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status", null = True)
    trait = models.ForeignKey(Trait, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_trait", null = True)
