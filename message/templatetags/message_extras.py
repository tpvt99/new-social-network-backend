from django import template
register = template.Library()

from message.models import MessageUser
from django.utils import timezone

@register.filter
def message_buddy(request_user, chat_buddy):
    if len(chat_buddy) == 2:
        for i in chat_buddy:
            if i != request_user:
                return i

@register.filter
def last_message(chat_buddy):
    t = chat_buddy.message_message_chat_buddies.all().order_by('-create_time')[0]
    return t

@register.filter
def message_user(user1, user2):
    chat_buddies = user1.message_messageuser_user.all()
    for i in chat_buddies:
        if user1 in i.user.all() and user2 in i.user.all() and len(i.user.all()) == 2:
            return i.id
    m = MessageUser.objects.create(last_active = timezone.now())
    m.user.add(user1)
    m.user.add(user2)
    m.save()
    return m.id
