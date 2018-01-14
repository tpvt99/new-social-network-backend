from django.conf.urls import url

from .views import Create, Join

app_name = 'plan'

urlpatterns = [
        url(r'^create/$', Create.as_view(), name='create'),

        url(r'^join/$', Join.as_view(), name='join'),
        ]
