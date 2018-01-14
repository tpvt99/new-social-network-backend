from django.conf.urls import url
from .views import Home, Status,Comment, Vote
from .views import SpecificContent, Content

app_name = 'anonymous'

urlpatterns = [
        url(r'^$', Home.as_view(), name='anonymous'),
        url(r'^status/$',Status.as_view(), name='status'),
        url(r'^comment/$', Comment.as_view(), name='comment'),
        url(r'^content/$', Content.as_view(), name='content'),
        url(r'^vote/$', Vote.as_view(), name='vote'),
        url(r'^link/$', SpecificContent.as_view(), name='link')
        ]
