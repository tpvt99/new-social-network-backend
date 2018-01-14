from django.conf.urls import url
from .views import Authentication

app_name = 'user'

urlpatterns = [
    url(r'^auth1/$', Authentication.as_view(), name = 'auth')
]
