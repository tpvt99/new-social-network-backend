from django.db import models
from django.conf import settings

from page.models import City
from activity.models import Activity

# Create your models here.

def activitiespost_image_upload(instance, filename):
    return 'activity_{0}/activitiespost/{1}'.format(instance.activity.id, filename)

class ActivitiesPost(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activity")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    text = models.TextField(null = True)
    image = models.ImageField(upload_to = activitiespost_image_upload, null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    privacy = models.CharField(max_length = 100, null = True)

class ActivitiesPostFriend(models.Model):
    activitiespost = models.ForeignKey(ActivitiesPost, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activitiespost")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
    time_create = models.DateTimeField(auto_now_add = True)
