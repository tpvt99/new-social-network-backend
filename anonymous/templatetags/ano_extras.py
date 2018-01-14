from django import template
from anonymous.models import Post, Vote
from user.models import MyUser
from django.utils import timezone

register = template.Library()

@register.filter
def render(post_id, user_id):
    post = Post.objects.get(pk__exact = int(post_id))
    user = MyUser.objects.get(pk__exact = int(user_id))
    try:
        vote = Vote.objects.get(post = post, user = user)
        if vote.been_vote == True:
            return True
        else:
            return False
    except Vote.DoesNotExist:
        return False

@register.filter
def render_time(time_post):
    delta = timezone.now() - time_post
    return delta.total_seconds()
