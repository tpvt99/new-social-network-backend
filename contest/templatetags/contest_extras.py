from django import template
from contest.models import ContestFollow
from contest.models import Contest

register = template.Library()

@register.filter
def contest_follow(user, contest):
    try:
        ContestFollow.objects.get(user = user, contest = contest)
        return True
    except ContestFollow.DoesNotExist:
        return False

@register.filter
def total_contest(user, kind):
    if kind == 'all':
        cf = ContestFollow.objects.filter(user = user)
    else:
        cf = ContestFollow.objects.filter(user = user, contest__contest_type = kind)
    return {'contest':cf,'quantity':len(cf)}

