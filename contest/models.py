from django.db import models
from django.conf import settings

# Create your models here.

def contest_image_upload(instance, filename):
    return 'contest/{0}'.format(filename)

class Contest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    head = models.CharField(max_length = 200)
    des = models.TextField(null = True)
    #age
    age_begin = models.IntegerField(null=True)
    age_end = models.IntegerField(null=True)
    #province
    province = models.CharField(max_length = 100,null=True)
    province_unicode = models.CharField(max_length = 100,null=True)
    city_unicode = models.CharField(max_length = 100,null=True)
    #image
    image = models.ImageField(upload_to = 'media',null=True)
    timezone = models.IntegerField(default = 0)
    time_create = models.DateTimeField(auto_now_add = True,null=True)
    time_begin = models.DateTimeField(null = True)
    privacy = models.CharField(max_length = 100, null = True)
    #type 
    contest_type = models.CharField(max_length = 100, null = True)

def contestpost_image_upload(instance, filename):
    return 'contest_{0}/contestpost/{1}'.format(instance.id, filename)

class ContestPost(models.Model):
    contest = models.ForeignKey(Contest, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_contest")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    text = models.TextField()
    image = models.ImageField(upload_to = 'media', null = True)
    time = models.DateTimeField(auto_now_add = True)

class ContestFollow(models.Model):
    contest = models.ForeignKey(Contest, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_contest")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")

    class Meta:
        unique_together = ('contest','user')
