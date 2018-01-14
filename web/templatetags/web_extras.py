from django import template
import datetime
from django.utils import timezone
from friend.models import AddFriend
import math
from noti.models import Notification
from activity.models import Activity
from message.models import MessageUser

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    arg1 = str(arg1)
    arg2 = str(arg2)
    return arg1 + arg2

@register.filter
def render_time(time_post, tz):
    # time_post is the time that added timezone
    tz = int(tz)
    time_delta = datetime.timedelta(hours = tz)
    now = timezone.now() + time_delta
    denta_time = now - time_post
    if denta_time.days == 1:
        return {'value':'yesterday','time':time_post}
    elif denta_time.days > 1:
        return {'value':'no','time':time_post}
    else:
        t = str(denta_time)
        t_list = t.split(':')
        if int(t_list[0]) == 0:
            if int(t_list[1]) ==0:
                return {'value':'second','time':int(math.ceil(float(t_list[2])))}
            else:
                return {'value':'minute','time':int(t_list[1])}
        else:
            return {'value':'hour','time':int(t_list[0])}

@register.filter(expects_localtime = True)
def rendertime(time_post, tz):
    delta = datetime.timedelta(hours = int(tz))
    if tz > 0:
        timex = time_post + delta
    else:
        timex = time_post - delta
    return {'hour':timex.hour, 'minute' : timex.minute}

@register.filter
def deltatime(time_post):
    now = timezone.now()
    if now > time_post:
       delta = now - time_post
    else:
        delta = time_post - now
    return delta.total_seconds()

@register.filter
def friend_request(user):
    fr = AddFriend.objects.filter(receiver = user, is_friend = False, read = False)
    return len(fr)

@register.filter
def notification(user):
    x = Notification.objects.filter(user = user, read = False)
    return len(x)

@register.filter
def act_suggestion(user):
    return Activity.objects.filter(privacy = 'public')[0]

@register.filter
def first_name(name):
    t = name.split(" ");
    return t[0]

@register.filter
def message(user):
    return user.message_messageuser_user.all().filter(read = False)
