from django.conf.urls import url
from .views import Online
from .views import TabFollowers

app_name = 'account'

urlpatterns = [
    url(r'^on$', Online.as_view(), name = 'on'),

    url(r'^tab_followers$', TabFollowers.as_view(), name = 'tab')
]
