from django import template

register = template.Library()
from activity.models import Activity, ActivityParticipants
from act.models import Act


@register.filter
def total_act(user,typex):
    a = Act.objects.filter(user = user, act_type = typex)
    c = Activity.objects.filter(activity_activityparticipants_activity__person = user, activity_activityparticipants_activity__accepted = True, activity_type = typex)
    return len(a) + len(c)

@register.filter
def act_filter(user,typex):
    return Act.objects.filter(user=user,act_type=typex)
