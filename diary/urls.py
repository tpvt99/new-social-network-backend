from django.conf.urls import url

app_name = 'diary'

from .views import Create, Content

urlpatterns = [
        url(r'create/$', Create.as_view(), name='create'),
        url(r'content/$', Content.as_view(), name='content'),
        ]


