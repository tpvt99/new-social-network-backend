from django.db import models
from django.conf import settings
from activity.models import Activity, ActivityParticipants, ActivityPostComment
from anonymous.models import Post as AnonymousPost
from anonymous.models import Vote as AnonymousVote
from anonymous.models import Comment as AnonymousComment
from event.models import Event, EventParticipants, EventPostComment
from anonymous.models import Post as AnonymousPost
from anonymous.models import Vote as AnonymousVote
from anonymous.models import Comment as AnonymousComment
from contest.models import Contest, ContestPost
from status.models import Status, StatusComment
from act.models import ActPost, Act
from activities.models import ActivitiesPost
from post.models import Post
from events.models import EventsPost
from trait.models import Trait
from group.models import Group, GroupInvitation
from user.models import User

# Create your models here.

KIND_OF_NOTIFICATION = {
        'activity':'activity',
        'activity-a':'join from guess',
        'activity-b':'invite from host',
        'a': 'invitation to join activity from host',
        'aa': 'accepted from host to join an activity',
        'ab':'declined from host to join an activity',
        'ac':'join activity from a guess',
        'ad':'declined from a guess which sent invitation to join activity',
        'ae':'accepted from guess to join',
        'b': 'like an anonymous post',
        'c': 'comment an anonymous post',
        'd': 'response from host of activity which was send',

        'activity':'activity',
        'activity-a':'join from guess',
        'activity-b':'invite form host',
        'activity-c':'decline from host', #decline is different from refuse
        'activity-d':'decline from guess',
        'activity-e':'accept from host',
        'activity-f':'accept from guess',
        'activity-g':'refuse from host',
        'activity-h':'refuse from guess',
        'activity-i':'activity report',
        'activity-j':'an activity post created',
        'activity-k':'a comment of an activity post',

        'event':'event',
        'event-a':'join from guess',
        'event-b':'invite form host',
        'event-c':'decline from host', #decline is different from refuse
        'event-d':'decline from guess',
        'event-e':'accept from host',
        'event-f':'accept from guess',
        'event-g':'refuse from host',
        'event-h':'refuse from guess',
        'event-i':'event report',
        'event-j':'an activity post created',
        'event-k':'a comment of an activity post',

        'anonymous':'anonymous',
        'anonymous-a':'somebody like your post',
        'anonymous-b':'somebody comment on your post',

        'contest':'create a contest',
        'contest-a':'contestpost in a contest',

        'status':'status',
        'status-a':'somebody react your status',
        'status-b':'somebody comment your status',
        'status-c':'somebody react your comment of a status',
        'status-d':'somebody comment your comment of a status',
        'status-e':'somebody create a plustag on a post',

        'act':'act',
        'act-a':'tag a friend in an act',
        'act-b':'tag a friend in an actpost',

        'activities':'activities',
        'activities-a':'tag a friend in a private activities post of activity',

        'post':'post',
        'post-a':'tag a friend in a post',

        'events':'events',
        'events-a':'tag a friend in a private events post of event',

        'trait':'trait',
        'trait-a':'create a trait for friend',

        'group':'group',
        'group-a' : 'invite from owner',
        'group-b' : 'invite from guess',
        'group-c' : 'accept from owner',
        }

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    noti_type = models.CharField(max_length = 100)
    read = models.BooleanField(default = False)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ANotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activityparticipants = models.ForeignKey(ActivityParticipants, on_delete = models.CASCADE)

class BNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    post = models.ForeignKey(AnonymousPost, on_delete = models.CASCADE)
    vote = models.ForeignKey(AnonymousVote, on_delete = models.CASCADE)

class CNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    post = models.ForeignKey(AnonymousPost, on_delete = models.CASCADE)
    comment = models.ForeignKey(AnonymousComment, on_delete = models.CASCADE)

class DNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activityparticipants = models.ForeignKey(ActivityParticipants, on_delete = models.CASCADE)

class EventNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

class EventANotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    eventparticipants = models.ForeignKey(EventParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class EventBNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    eventparticipants = models.ForeignKey(EventParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class EventCNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)
    time_send = models.DateTimeField(null = True)

class EventDNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    guess = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_guess", null = True)
    time = models.DateTimeField(auto_now_add = True, null = True)
    time_send = models.DateTimeField(null = True)

class EventENotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    eventparticipants = models.ForeignKey(EventParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class EventFNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    eventparticipants = models.ForeignKey(EventParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class EventGNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class EventHNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    guess = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_guess", null = True)
    time = models.DateTimeField(auto_now_add = True, null = True)

class EventINotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

class EventJNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)

class EventKNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    eventpostcomment = models.ForeignKey(EventPostComment, on_delete = models.CASCADE)

class ActivityNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)

class ActivityANotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activityparticipants = models.ForeignKey(ActivityParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ActivityBNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activityparticipants = models.ForeignKey(ActivityParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ActivityCNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)
    time_send = models.DateTimeField(null = True)

class ActivityDNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    guess = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_guess", null = True)
    time = models.DateTimeField(auto_now_add = True, null = True)
    time_send = models.DateTimeField(null = True)

class ActivityENotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activityparticipants = models.ForeignKey(ActivityParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ActivityFNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activityparticipants = models.ForeignKey(ActivityParticipants, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ActivityGNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ActivityHNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    guess = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_guess", null = True)
    time = models.DateTimeField(auto_now_add = True, null = True)

class ActivityINotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)

class ActivityJNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)

class ActivityKNotification(models.Model):
    noti = models.ForeignKey(Notification, on_delete = models.CASCADE)
    activitypostcomment = models.ForeignKey(ActivityPostComment, on_delete = models.CASCADE)

class AnonymousANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    ano_post = models.ForeignKey(AnonymousPost, on_delete = models.CASCADE)
    vote = models.ForeignKey(AnonymousVote, on_delete = models.CASCADE,null=True)

class AnonymousBNotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    ano_post = models.ForeignKey(AnonymousPost, on_delete = models.CASCADE)
    comment = models.ForeignKey(AnonymousComment, on_delete = models.CASCADE, null = True)

class ContestNotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete = models.CASCADE)

class ContestANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    contestpost = models.ForeignKey(ContestPost, on_delete = models.CASCADE)

class StatusANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_noti")
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)

class StatusBNotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_noti")
    status = models.ForeignKey(Status, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_status")
    statuscomment = models.OneToOneField(StatusComment, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user", null = True)

class ActANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    act = models.ForeignKey(Act, on_delete = models.CASCADE, null = True)

class ActBNotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    actpost = models.ForeignKey(ActPost, on_delete = models.CASCADE)

class ActivitiesANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    activitiespost = models.ForeignKey(ActivitiesPost, on_delete = models.CASCADE)

class EventsANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    event = models.ForeignKey(Event , on_delete = models.CASCADE)
    eventspost = models.ForeignKey(EventsPost , on_delete = models.CASCADE)

class PostANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    post = models.ForeignKey(Post , on_delete = models.CASCADE)

class TraitANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    trait = models.ForeignKey(Trait, on_delete = models.CASCADE)

class GroupANotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    groupinvitation = models.OneToOneField(GroupInvitation, on_delete = models.CASCADE, null = True)

class GroupBNotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    groupinvitation = models.OneToOneField(GroupInvitation , on_delete = models.CASCADE, null = True)

class GroupCNotification(models.Model):
    noti = models.OneToOneField(Notification, on_delete = models.CASCADE)
    group = models.OneToOneField(Group, on_delete = models.CASCADE)
