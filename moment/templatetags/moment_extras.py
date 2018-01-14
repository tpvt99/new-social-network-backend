from django import template
register = template.Library()

from moment.models import Moment
from plustag.models import PlustagLife
from plustag.models import plus_tag

@register.filter
def total_plustag_of_specific_moment(moment):
    t = PlustagLife.objects.filter(moment = moment)
    x = []
    for i in plus_tag:
        x.append({'tag':i,'quantity':len(PlustagLife.objects.filter(moment = moment, plustag_type = i))})
    return x
