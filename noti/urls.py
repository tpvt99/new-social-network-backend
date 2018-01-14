from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import FetchNoti

app_name = 'noti'

urlpatterns = [

    url(r'^noti/fetch$', FetchNoti.as_view(), name = 'fetch'),

    ]
