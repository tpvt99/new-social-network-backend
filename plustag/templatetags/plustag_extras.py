from django import template
register = template.Library()

from plustag.models import PlustagLife
from django.utils import timezone
import datetime
from django.db.models import Q
from plustag.models import plus_tag
import re

def return_total(user, kind):
    today = timezone.now()
    begin_month = timezone.make_aware(datetime.datetime(today.year,today.month,1))
    if today.month == 12:
        end_month = timezone.make_aware(datetime.datetime(today.year+1,1,1))
    else:
        end_month = timezone.make_aware(datetime.datetime(today.year,today.month+1,1))
    a = PlustagLife.objects.filter(Q(create_time__gte = begin_month) & Q(create_time__lte = end_month), user_receive_plus = user, plustag_type = kind)
    total_percent = 0
    for i in a: #just status
        if i.status: 
            if i.status.percent != 0:
                total_percent += i.status.percent
            else:
                total_percent += 15
        elif i.moment:
            total_percent += 25
    return total_percent*100/5000

@register.filter
def total_plustag(user, kind):
    return return_total(user, kind)

@register.filter
def total_plustag_order(user, kind):
    friend = user.friend_friend_user.all()
    order = []
    for i in friend:
        order.append({'user':i.friend,'quantity':return_total(i.friend, kind)})
    order.append({'user':user,'quantity':return_total(user, kind)})
    return sorted(order, key = lambda x : x['quantity'], reverse = True)


@register.filter
def style_plustag(text):
    re_result = re.sub(r'(^\+[a-z]+)|( \+[a-z]+)',r'<span style="color:#e74c3c;">\1\2</span>', text)
    return re_result

@register.filter
def escape_plustag(text):
    new_text = ''
    for i in text:
        if i == '<':
            new_text += '&lt;'
        elif i == '>':
            new_text += '&gt;'
        elif i == "'":
            new_text += '&#39;'
        elif i == '&':
            new_text += '&amp;'
        else:
            new_text += i
    return new_text
