from django.db import models
from user.models import MyUser
from django.conf import settings

from page.models import City

# Create your models here.

class Plan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    name = models.CharField(max_length = 100, null = True)
    des = models.TextField(null = True)
    image = models.ImageField(upload_to = 'media', null = True)
    time = models.DateTimeField(null = True)
    create_time = models.DateTimeField(auto_now_add = True)
    city = models.ForeignKey(City, on_delete = models.CASCADE, null = True)
    city_code = models.CharField(max_length = 100, null = True)
    address = models.CharField(max_length = 100, null = True)
    share = models.IntegerField()
    time_year = models.BooleanField(default = False)
    time_month = models.BooleanField(default = False)
    time_day = models.BooleanField(default = False)
    time_hour = models.BooleanField(default = False)
    time_minute = models.BooleanField(default = False)
    timezone = models.IntegerField(null = True)

class PlanParticipants(models.Model):
    plan = models.OneToOneField(Plan, on_delete = models.CASCADE)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through = 'ParticipantMoreInfo', related_name = "%(app_label)s_%(class)s_participants", through_fields = ('planparticipants','person'),)

class ParticipantMoreInfo(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "%(app_label)s_%(class)s_person")
    planparticipants = models.ForeignKey(PlanParticipants, related_name = "%(app_label)s_%(class)s_participants")
    plan = models.ForeignKey(Plan, related_name = "%(app_label)s_%(class)s_plan")
    is_join = models.BooleanField(default = False)
    owner_invited = models.BooleanField(default = False)
    user_invited = models.BooleanField(default = False)
    time_join = models.DateTimeField(auto_now_add = True, null = True)

    class Meta:
        unique_together = ('person','planparticipants','plan')
