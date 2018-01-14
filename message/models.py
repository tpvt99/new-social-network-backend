from django.db import models
from django.conf import settings
from user.models import User

# Create your models here.

class MessageUser(models.Model):
    users = models.ManyToManyField(User, related_name = "%(app_label)s_%(class)s_user")
    last_active = models.DateTimeField(null = True)
    # user or group to allow more user in group or not
    message_type = models.CharField(max_length = 10, default = 'user')

class MessageUserInfo(models.Model):
    frame = models.ForeignKey(MessageUser, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_frame")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    read = models.BooleanField(default = True)
    fetch = models.BooleanField(default = True)

class Message(models.Model):
    user_send = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_usersend")
    chat_frame = models.ForeignKey(MessageUser, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_chat_buddies")
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)

class MessageReadInfo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    message = models.ForeignKey(Message, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_message")
    read = models.BooleanField(default = False)
    fetch = models.BooleanField(default = False)
