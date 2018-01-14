from django.db import models
from django.conf import settings

# Create your models here.

def upload_image(instance, filename):
    return 'user_{0}/moment/{1}'.format(instance.user.id, filename)

class Moment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, related_name="%(app_label)s_%(class)s_user")
    text = models.CharField(max_length = 100, null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = upload_image)
    privacy = models.TextField(max_length = 100)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, related_name="%(app_label)s_%(class)s_user")
    moment = models.ForeignKey(Moment, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_moment")
    time_create = models.DateTimeField(auto_now_add = True)
    been_vote = models.BooleanField(default = False)

    class Meta:
        unique_together = ('user','moment')

class MomentComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    moment = models.ForeignKey(Moment, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_moment")
    comment = models.CharField(max_length = 200)
    time_create = models.DateTimeField(auto_now_add = True)
