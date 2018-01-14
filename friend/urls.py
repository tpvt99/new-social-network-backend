#urls 

from django.conf.urls import url

# views

from .views import AddFriend, FriendAjax
from .views import FriendRequest, FriendTag


app_name = 'friend'

urlpatterns = [
        url(r'^add/$', AddFriend.as_view(), name='addfriend'),

        url(r'^request/$', FriendRequest.as_view(), name='request'),

        url(r'^friendajax/$', FriendAjax.as_view(), name='ajax'),
    
        url(r'^tag$', FriendTag.as_view(), name='friendtag')
        ]

