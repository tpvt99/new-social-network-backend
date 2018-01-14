from django.db import models
from django.conf import settings
from activity.models import Activity

# Create your models here.

def act_image_upload(instance, filename):
    return 'act/{0}'.format(filename)

class Act(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    head = models.CharField(max_length = 200, null = True) #2
    des = models.TextField(null = True) #2
    province = models.CharField(max_length = 200, null = True) #2
    province_unicode = models.CharField(max_length = 200, null = True) #2
    image = models.ImageField(upload_to = act_image_upload , null = True)
    privacy = models.CharField(max_length = 100, null = True)
    act_approved = models.BooleanField(default = False)
    is_used = models.BooleanField(default = False) # whether this act is added into lifepage
    act_type = models.CharField(max_length = 100, null = True) #act type for show in lifepage

class ActFriend(models.Model):
    act = models.ForeignKey(Act, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_act")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    accepted = models.BooleanField(default = 0)

def actpost_image_upload(instance, filename):
    return 'actpost_{0}/{1}'.format(instance.act.id, filename)

class ActPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    act = models.ForeignKey(Act, on_delete = models.CASCADE)
    time_create = models.DateTimeField(auto_now_add = True)
    des = models.TextField()
    image = models.ImageField(upload_to = actpost_image_upload , null = True)
    privacy = models.CharField(max_length = 100)

class ActPostTagFriend(models.Model):
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    actpost = models.ForeignKey(ActPost, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_actpost", null = True)
    time_create = models.DateTimeField(auto_now_add = True)

class ActPostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    act = models.ForeignKey(Act, on_delete = models.CASCADE)
    time_create = models.DateTimeField(auto_now_add = True)
    comment = models.CharField(max_length = 200)
