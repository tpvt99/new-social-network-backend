from account.models import NewFeed
from django.core.exceptions import ObjectDoesNotExist

def newfeed_serialize(user):
    try:
        newfeed = user.newfeed
    except ObjectDoesNotExist:
        newfeed = NewFeed.objects.create(user = user)
    return {
            'isMinimizedFeed': newfeed.isMinimizedFeed
    }
