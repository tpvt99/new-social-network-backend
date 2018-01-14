#urls

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# view

from .views import Activities, FriendAjax, Create

app_name = 'activities'

urlpatterns = [

    url(r'^activities/fraj/$', FriendAjax.as_view(), name='friendajax'),

    url(r'^create/$', Create.as_view(), name='create'),

    url(r'^$',Activities.as_view(), name='activities'),


    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
