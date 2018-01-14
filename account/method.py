from .models import OnlineTime
from django.utils import timezone
from django.db.utils import IntegrityError

def set_online_time(user):
    try:
        a = OnlineTime.objects.create(user = user)
    except IntegrityError:
        a = OnlineTime.objects.get(user = user)
        a.time = timezone.now()
        a.save()
