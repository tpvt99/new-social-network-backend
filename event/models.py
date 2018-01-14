from django.db import models
from django.conf import settings

# Create your models here.

def event_upload_path(instance, filename):
    return 'event/{0}'.format(filename)

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    head = models.CharField(max_length = 100)
    des = models.TextField()
    image = models.ImageField(upload_to = event_upload_path , null = True)

    #place
    province = models.CharField(max_length = 100, null = True)
    province_unicode = models.CharField(max_length = 100, null = True)
    city = models.CharField(max_length = 100, null = True)
    city_unicode = models.CharField(max_length = 100, null = True)
    address = models.CharField(max_length = 100, null = True)
    #time
    time_begin = models.DateTimeField(null = True)
    time_end = models.DateTimeField(null = True)
    #age
    age_begin = models.IntegerField(null = True)
    age_end = models.IntegerField(null = True)
    # fee
    fee = models.IntegerField(null=True, default=0)
    fee_des = models.TextField(null=True)
    #quantity
    quantity = models.IntegerField(default = 0)
    time_create = models.DateTimeField(auto_now_add = True)

    # privacy
    privacy = models.CharField(max_length=100, null = True)
    event_type = models.CharField(max_length=100, null = True)
    #report
    report = models.IntegerField(default = 0)

class EventSport(models.Model):
    event = models.ManyToManyField(Event,related_name="%(app_label)s_%(class)s_event")
    sport_type = models.CharField(max_length = 100)
    sport_type_unicode = models.CharField(max_length=100)

class EventMusic(models.Model):
    event = models.ManyToManyField(Event, related_name="%(app_label)s_%(class)s_event")
    music_type = models.CharField(max_length = 100)
    music_type_unicode = models.CharField(max_length = 100)

class EventParticipants(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    event = models.ForeignKey(Event, on_delete= models.CASCADE, related_name = "%(app_label)s_%(class)s_event")
    owner_invite = models.BooleanField(default = False)
    guess_invite = models.BooleanField(default = False)
    accepted = models.BooleanField(default = False)
    time_create = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        unique_together = ('user','event')

class EventReport(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    time = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = ('event','user')

def eventpost_image_upload(instance, filename):
    return 'event_{0}/eventpost/{1}'.format(instance.event.id, filename)

class EventPost(models.Model):
    event = models.ForeignKey(Event , on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_event")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    text = models.TextField(null = True)
    image = models.ImageField(upload_to = eventpost_image_upload , null = True)
    time = models.DateTimeField(auto_now_add = True)

class EventPostComment(models.Model):
    eventpost = models.ForeignKey(EventPost, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_eventpost")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
