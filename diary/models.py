from django.db import models
from django.conf import settings

# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    diary = models.TextField()
    image = models.ImageField(upload_to = 'media', null = True)
    place = models.CharField(max_length = 100, null = True)
    create_time = models.DateTimeField(auto_now_add = True)
    timezone = models.IntegerField()
