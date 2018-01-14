from django.db import models
from django.conf import settings
from status.models import Status
from moment.models import Moment
from user.models import User

# Create your models here.

plus_tag = ['+chat','+dep','+ngau']

class PlustagLife(models.Model):
    user_receive_plus = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user_receive_plus", null = True)
    user_send_plus = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user_send_plus")
    status = models.ForeignKey(Status,on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_status", null = True)
    moment = models.ForeignKey(Moment ,on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_moment", null = True)
    plustag_type = models.CharField(max_length = 100)
    create_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = (('user_send_plus','status','plustag_type'),('user_send_plus','moment','plustag_type'))

class Plustag(models.Model):
    user_receive_plus = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user_receive_plus", null = True)
    user_send_plus = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user_send_plus")
    status = models.ForeignKey(Status,on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_status", null = True)
    plustag_name = models.CharField(max_length = 30)
    create_time = models.DateTimeField(auto_now_add = True)
    votes = models.PositiveIntegerField(default = 0)

    class Meta:
        unique_together = ('status','plustag_name')

class PlustagVote(models.Model):
    plustag = models.ForeignKey(Plustag, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_plustag")
    user_vote = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user_vote")
    been_vote = models.BooleanField(default = False)
    time = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user_vote','plustag')
