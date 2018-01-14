from django import template

register = template.Library()

from activity.models import Activity, ActivityParticipants
from act.models import Act

@register.filter
def total_activities(user):
    a = Act.objects.filter(user = user)
    c = ActivityParticipants.objects.filter(person = user, accepted = True)
    return len(a) + len(c)
