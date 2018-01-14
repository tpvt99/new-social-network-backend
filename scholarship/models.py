from django.db import models
from django.conf import settings

# Create your models here.

class ScholarshipTarget(models.Model):
    # YOU MUST GENERATE THIS DATA
    # --------------------------
    name = models.CharField(max_length = 50)

class Scholarship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #create page
    head = models.CharField(max_length = 100, null = True)
    target = models.ManyToManyField(ScholarshipTarget)
    target_des = models.TextField(null = True)
    content = models.TextField(null = True)
    prize = models.TextField(null = True)
    time_begin = models.DateTimeField(null = True) #  UTC
    time_end = models.DateTimeField(null = True)  #  UTC
    create_time = models.DateTimeField(auto_now_add = True)
    timezone = models.IntegerField(null = True)

