from django import template

register = template.Library()

from event.models import Event, EventParticipants

@register.filter
def total_events(user):
    e = EventParticipants.objects.filter(user = user, accepted = True)
    return len(e)
