from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Events, Create

app_name = 'events'

urlpatterns = [
    url(r'^$', Events.as_view(), name='events'),

    url(r'^create/$', Create.as_view(), name='create'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
