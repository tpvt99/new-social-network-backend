from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Activity, FriendAjax
from .views import Create, ActPost
from .views import UpdateImage
app_name = 'act'

urlpatterns = [
        url(r'^act/(?P<id>[0-9]+)/$', Activity.as_view(), name='act'),

        url(r'^ajax/friend/$', FriendAjax.as_view(), name='friendajax'),

        url(r'^create/$', Create.as_view(), name='create'),

        url(r'^actpost/create/$', ActPost.as_view(), name='actpost'),

        url(r'^updateimage/$', UpdateImage.as_view(), name='update'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
