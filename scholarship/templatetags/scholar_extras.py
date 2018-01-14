from django import template
from datetime import timedelta
from django.utils import timezone

register = template.Library()

@register.filter
def render_time(time_post, tz):
    tz = int(tz)
    delta = timedelta(hours = tz)
    return time_post + delta
