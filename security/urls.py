from django.conf.urls import url

from .views import CsrfToken
from .views import CheckAuthentication
from .views import CheckNetworkAuthentication

urlpatterns = [
    url(r'^csrf$', CsrfToken.as_view(), name='csrf'),

    url(r'^auth$', CheckAuthentication.as_view(), name='check'),

    url(r'^netauth$', CheckNetworkAuthentication.as_view(), name = 'network')
    ]
