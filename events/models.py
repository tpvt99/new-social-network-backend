from django.db import models
from django.conf import settings

from event.models import Event

# Create your models here.

def eventspost_image_upload(instance, filename):
    return 'event_{0}/eventspost/{1}'.format(instance.event.id, filename)

class EventsPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    text = models.TextField(null = True)
    image = models.ImageField(upload_to = eventspost_image_upload, null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    privacy = models.CharField(max_length = 100, null = True)

class EventsPostFriend(models.Model):
    eventspost = models.ForeignKey(EventsPost, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_eventspost")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
    time_create = models.DateTimeField(auto_now_add = True)
