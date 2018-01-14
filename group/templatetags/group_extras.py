from django import template
register = template.Library()
from group.models import GroupMember
from group.models import GroupInvitation

@register.filter
def group_type(user,group):
    t = GroupMember.objects.get(user = user, group= group)
    return t.group_type

@register.filter
def is_follow(user,group):
    t = GroupMember.objects.get(user = user, group= group)
    return t.follow

@register.filter
def render_member_button(user, group):
    try:
        x = GroupInvitation.objects.get(user = user, group = group)
        if x.is_member == True:
            return 'yes'
        else:
            if x.guess_invite == True:
                return 'guess'
            return 'owner'
    except GroupInvitation.DoesNotExist:
        return 'no'

@register.filter
def member_request(group):
    return GroupInvitation.objects.filter(group = group, is_member = False)
