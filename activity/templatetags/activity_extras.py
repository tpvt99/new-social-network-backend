from django import template
from activity.models import Activity, ActivityParticipants, ActivityReport
from activity.models import ActivityPost, ActivityPostComment

from act.models import Act

register = template.Library()

from django.utils import timezone

@register.filter
def quantity(act_id):
    activity = Activity.objects.get(pk__exact = int(act_id))
    ap = activity.activity_activityparticipants_activity.filter(accepted = True).exclude(person = activity.user)
    result = dict()
    result['len'] = len(ap)
    result['m'], result['f'] = 0,0
    for i in ap:
        if i.person.info.sex == 'male':
            result['m'] +=  1
        elif i.person.info.sex == 'female':
            result['f'] +=  1
    return result

@register.filter
def render_join(activity, user):
    try:
        ap = ActivityParticipants.objects.get(activity = activity, person = user)
        if ap.accepted == True:
            return 'true'
        else:
            return 'wait'
    except ActivityParticipants.DoesNotExist:
        return 'false'

@register.filter
def render_participate_button(activity, user):
    try:
        ap = ActivityParticipants.objects.get(activity = activity, person = user)
        if ap.accepted == True:
            if ap.activity.user == user:
                return 'host'
            else:
                return 'ok'
        else:
            if ap.owner_invite == True:
                return 'owner'
            else:
                return 'guess'
    except ActivityParticipants.DoesNotExist:
        if user != activity.user:
            return 'join'
        else:
            return 'invite'

@register.filter
def activityparticipants(activity,a):
    if a == 1:
        return activity.activity_activityparticipants_activity.filter(accepted = True)
    else:
        return activity.activity_activityparticipants_activity.filter(accepted = False)

@register.filter
def addslash(head):
    return '-'.join(head.split(' '))

@register.filter
def invite_friend(friend, activity):
    try:
        ap = ActivityParticipants.objects.get(person = friend, activity = activity)
        if ap.accepted == False:
            if ap.guess_invite == True:
                return {'stat':'wait', 'key':'guess'}
            else:
                return {'stat':'wait', 'key':'owner'}
        else:
            return {'stat':'accepted'}
    except ActivityParticipants.DoesNotExist:
        return {'stat':'invite'}

@register.filter
def who_accept(user, activity):
    ap = ActivityParticipants.objects.get(person = user, activity = activity, accepted = False)
    if ap.owner_invite == True:
        return True
    return False

@register.filter
def render_report(activity, user):
    try:
        ActivityReport.objects.get(activity = activity, user = user)
        return True
    except ActivityReport.DoesNotExist:
        return False

@register.filter
def outgoing_activity(user):
    t = Activity.objects.filter(activity_activityparticipants_activity__person = user ,activity_activityparticipants_activity__accepted = True, time_begin__gte = timezone.now())
    return t

@register.filter
def outgoing_activity_group(group):
    t = Activity.objects.filter(group=group,time_begin__gte = timezone.now())
    return t

@register.filter
def total_activity(user,kind):
    if kind == 'all':
        t = Activity.objects.filter(activity_activityparticipants_activity__person = user, activity_activityparticipants_activity__accepted = True)
    else:
        t = Activity.objects.filter(activity_activityparticipants_activity__person = user, activity_activityparticipants_activity__accepted = True, activity_type = kind)
    return {'quantity':len(t),'activity':t}

@register.filter
def total_activity_order(request_user, kind):
    friend = request_user.friend_friend_user.all()
    order = []
    for i in friend:
        if kind == 'all':
            order.append({'user':i.friend,'quantity':len(Activity.objects.filter(activity_activityparticipants_activity__person = i.friend, activity_activityparticipants_activity__accepted=True))+len(Act.objects.filter(user=i.friend, act_type=kind))})
        else:
            order.append({'user':i.friend,'quantity':len(Activity.objects.filter(activity_activityparticipants_activity__person = i.friend, activity_activityparticipants_activity__accepted=True, activity_type=kind))+len(Act.objects.filter(user=i.friend,act_type=kind))})
    order.append({'user':request_user,'quantity':len(Activity.objects.filter(activity_activityparticipants_activity__person = request_user, activity_activityparticipants_activity__accepted=True, activity_type=kind))+len(Act.objects.filter(user=request_user,act_type=kind))})
    return sorted(order, key = lambda x: x['quantity'], reverse = True)
