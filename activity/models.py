from django.db import models
from django.conf import settings
from page.models import City
from group.models import Group

# Create your models here.

def activity_upload_path(instance , filename):
    return 'activity/{0}'.format(filename)

class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_group", null = True)
    head = models.CharField(max_length = 100, null = True)
    des = models.TextField(null = True)
    #type
    activity_type = models.CharField(max_length = 100, null = True)
    # time
    time_begin = models.DateTimeField(null = True)
    time_end = models.DateTimeField(null = True)
    #place
    province = models.CharField(max_length = 100, null = True)
    province_unicode = models.CharField(max_length = 100, null = True)
    city = models.CharField(max_length = 100, null=True)
    address = models.CharField(max_length = 100, null = True)
    #age
    age1 = models.IntegerField(null = True)
    age2 = models.IntegerField(null = True)
    #sex
    sex = models.CharField(max_length = 10, null = True)
    #fee
    fee = models.IntegerField(null = True)
    # quantity of people
    quantity = models.IntegerField(null = True)
    # image
    image = models.ImageField(upload_to = activity_upload_path, null = True)
    # create date
    time_create = models.DateTimeField(auto_now_add = True)
    timezone = models.IntegerField(default = 0)
    #privacy
    privacy = models.CharField(max_length = 100)
    #spam 
    report = models.IntegerField(default = 0)

class ActivityParticipants(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_person")
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activity")
    owner_invite = models.BooleanField(default = False)
    guess_invite = models.BooleanField(default = False)
    accepted = models.BooleanField(default = False)
    time_create = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        unique_together = ('person','activity')

class ActivitySport(models.Model):
    activity = models.ManyToManyField(Activity, related_name = "%(app_label)s_%(class)s_activity")
    type_of_sport = models.CharField(max_length = 100);
    type_of_sport_unicode = models.CharField(max_length = 100, null = True)

class ActivityEsport(models.Model):
    activity = models.ManyToManyField(Activity, related_name = "%(app_label)s_%(class)s_activity")
    type_of_esport = models.CharField(max_length = 100);
    type_of_esport_unicode = models.CharField(max_length = 100)

class ActivityMusic(models.Model):
    activity = models.ManyToManyField(Activity, related_name = "%(app_label)s_%(class)s_activity")
    type_of_music = models.CharField(max_length = 100);
    type_of_music_unicode = models.CharField(max_length = 100)

class ActivityReport(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activity")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    time = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('activity', 'user')

def activitypost_image_upload(instance, filename):
    return 'activity_{0}/activitypost/{1}'.format(instance.id, filename)

class ActivityPost(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activity")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    text = models.TextField(null = True)
    image = models.ImageField(upload_to = activitypost_image_upload , null = True)
    time = models.DateTimeField(auto_now_add = True)

class ActivityPostFriend(models.Model):
    activitypost = models.ForeignKey(ActivityPost, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activitypost")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_friend")
    time_create = models.DateTimeField(auto_now_add = True)

class ActivityPostComment(models.Model):
    activitypost = models.ForeignKey(ActivityPost, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_activitypost")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
