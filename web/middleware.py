import pytz

from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timzone')
        if tzname:
            timezone.activiate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
