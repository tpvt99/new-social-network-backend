from django.conf.urls import url

from .views import Create, Content
app_name = 'scholarship'

urlpatterns = [
        url(r'^create/$' , Create.as_view(), name='create'),
        url(r'^content/$', Content.as_view(), name='content'),
        ]
