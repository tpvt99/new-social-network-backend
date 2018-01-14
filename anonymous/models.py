from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    des = models.TextField()
    user_des = models.CharField(max_length = 100)
    heart = models.IntegerField(default = 0)
    time = models.DateTimeField(auto_now_add = True, null = True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete =models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    user_des = models.CharField(max_length=20)
    des = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    is_anonymous = models.BooleanField(default = 0) #1 is anonymous, #0 is not anonymous

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    been_vote = models.BooleanField(default = False)
    class Meta:
        unique_together = ('user','post')
