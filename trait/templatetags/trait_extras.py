from django import template

register = template.Library()

from trait.models import Trait

@register.filter
def trait(user):
    t = Trait.objects.filter(user_receive = user)
    result = {}
    for i in t:
        result[i.trait_type] = result.setdefault(i.trait_type,0) + 1
    return result

@register.filter
def total_trait(user,kind):
    t = Trait.objects.filter(user_receive = user, trait_type = kind)
    return {'trait':t,'quantity':len(t)}

@register.filter
def total_trait_order(user, kind):
    friend = user.friend_friend_user.all()
    order = []
    for i in friend:
        order.append({'user':i.friend,'quantity':len(Trait.objects.filter(user_receive = i.friend, trait_type = kind))})
    order.append({'user':user, 'quantity':len(Trait.objects.filter(user_receive = user, trait_type = kind))})
    return sorted(order, key = lambda x : x['quantity'], reverse = True)
