from django.db import models
from django.conf import settings

from act.models import Act, ActPost
from activity.models import Activity, ActivityPost
from activities.models import ActivitiesPost
from event.models import Event, EventPost
from post.models import Post
from events.models import EventsPost
from contest.models import Contest, ContestPost
from trait.models import Trait
from group.models import GroupPost
from group.models import Group
from user.models import User

STATUS_TYPE = {
    'post': 'A user has create a new feed post'
}

# Create your models here.

class Status(models.Model):
    #1 who post the status, now it is 2 is user and page presenting a user post in page. Who post is different from who owner in which owner represents where they will be show in newfeeds
    # who post will have 2 choice is user or page
    who_post = models.CharField(max_length = 20, default = 'user')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)
    # page = models.ForeignKey(Page, on_delete = models.CASCADE, related_name = "%(app_labels)_%(class)s_page", null = True)

    
    # owner of status is the status is belong to. For example, if post is created in group so the owner is group but who_post is 'user', this is somehow the privacy of status
    # who_owner includes: user, group, page, team, meetup 
    # in one status, 2 below must not be empty or empty togeter.
    # if owner is user means that user create in timeline not in any specific group or team, then 2 below can be empty
    who_owner = models.CharField(max_length = 30, null = True)
    who_owner_id = models.IntegerField(null = True)


    #2 status_type must present
    time_create = models.DateTimeField(auto_now_add = True)
    # verb includes: post, sale, change_profile_picture, like, share, comment.
    verb = models.CharField(max_length = 30)

    #3 the data of status

    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, related_name="%(app_label)s_%(class)s_post")

    #4 privacy is public, private, friend or custom
    # custom means that you want to share with some friends of you
    
    # when status is created in group, team, meetup, page, event, activity, the privacy is just in that enclosed group
    privacy = models.CharField(max_length = 100, null = True)
    timeline = models.CharField(max_length = 100, null = True)

    #5 votes
    vote = models.IntegerField(default = 0)
    use_default_reaction = models.BooleanField(default = True)
    use_custom_reaction = models.BooleanField(default = False)

    #6 shares
    share = models.IntegerField(default = 0)


class StatusReaction(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status")
    reactionName = models.CharField(max_length = 30)
    reactionType = models.CharField(max_length = 10, null = True)
    icon = models.CharField(max_length = 50, null = True)
    vote = models.IntegerField(default = 0)

class StatusReactionVote(models.Model):
    statusreaction = models.ForeignKey(StatusReaction, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_statusreaction")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    been_vote = models.BooleanField(default = False)
    time_create = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = ('user','statusreaction')


class StatusVote(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status")
    been_vote = models.BooleanField(default = False)
    time_create = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user','status')

class StatusComment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status")
    comment = models.CharField(max_length = 200)
    time_create = models.DateTimeField(auto_now_add = True)

