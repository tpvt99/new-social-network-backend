from django.db import models
from django.conf import settings

# Create your models here.

def upload_group_pic(instance, filename):
    return 'group/group_{0}/{1}'.format(instance.group.id, filename)

class Group(models.Model):
    admin = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "%(app_label)s_%(class)s_admin")
    name = models.CharField(max_length = 200)
    privacy = models.CharField(max_length = 100) #public, private
    time_create = models.DateTimeField(auto_now_add = True)
    group_type = models.CharField(max_length = 100, null = True)

class GroupInfo(models.Model):
    group = models.OneToOneField(Group, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group")
    image = models.ImageField(upload_to = upload_group_pic, null = True)
    background = models.ImageField(upload_to = upload_group_pic, null = True)
    intro = models.TextField(null = True)

class GroupMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group")
    group_type = models.CharField(max_length = 100) # social, work, entertainment
    follow = models.BooleanField(default = True)
    join_time = models.DateTimeField(auto_now_add = True)

class GroupMemberDedication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group")
    group_member = models.ForeignKey(GroupMember, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group_member", null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    

class GroupInvitation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    who_invite = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_who_invite")
    guess_invite = models.BooleanField(default = False)
    owner_invite = models.BooleanField(default = False)
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group")
    time_invitation = models.DateTimeField(auto_now_add = True)
    group_member = models.ForeignKey(GroupMember, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_group_member", null = True)
    is_member = models.BooleanField(default = False)

    class Meta:
        unique_together=('user','group')

def upload_image_grouppost(instance, filename):
    return 'group/group_{0}/{1}'.format(instance.group.id, filename)

class GroupPost(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_group")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    text = models.TextField()
    image = models.ImageField(upload_to = upload_image_grouppost, null = True)
    time_create = models.DateTimeField(auto_now_add = True, null = True)
