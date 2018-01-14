from django.conf.urls import url

from .views import Create
app_name = 'goal'

urlpatterns = [
    url(r'^$', Create.as_view(), name='create'),
        ]
