from django import template
from django.utils import timezone

register = template.Library()
from event.models import Event, EventParticipants, EventReport

@register.filter
def quantity(event):
    ep = event.event_eventparticipants_event.filter(accepted = True).exclude(user = event.user)
    result = dict()
    result['len'] = len(ep)
    result['m'], result['f'] = 0,0
    for i in ep:
        if i.user.info.sex == 'male':
            result['m'] +=  1
        elif i.user.info.sex == 'female':
            result['f'] +=  1
    return result

@register.filter
def render_participate_button(event, user):
    try:
        ep = EventParticipants.objects.get(user = user, event = event)
        if ep.accepted == False:
            if ep.owner_invite == True:
                return 'owner'
            else:
                return 'guess'
        else:
            if ep.event.user == user:
                return 'host'
            else:
                return 'ok'
    except EventParticipants.DoesNotExist:
        if event.user != user:
            return 'join'
        else:
            return 'invite'

@register.filter
def report_render(event, user):
    try:
        EventReport.objects.get(event = event, user = user)
        return True
    except EventReport.DoesNotExist:
        return False

@register.filter
def event(user):
    return Event.objects.filter(event_eventparticipants_event__user = user, event_eventparticipants_event__accepted = True)

@register.filter
def total_event(user, kind):
    if kind == 'all':
        t = Event.objects.filter(event_eventparticipants_event__user = user, event_eventparticipants_event__accepted = True)
    else:
        t = Event.objects.filter(event_eventparticipants_event__user = user, event_eventparticipants_event__accepted = True, event_type = kind)
    return {'event':t,'quantity':len(t)}

@register.filter
def outgoing_event(user):
    return Event.objects.filter(event_eventparticipants_event__user = user, event_eventparticipants_event__accepted = True, time_begin__gte = timezone.now())
