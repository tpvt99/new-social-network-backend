# url

from django.conf.urls import url

# model

from .views import CreatePage

app_name = 'page'

urlpatterns = [
        url(r'^createpage/(?P<field>[a-z]+)/$', CreatePage.as_view(), name='createpage'),

]
