from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Create, Moment, Comment
app_name = 'moment'

urlpatterns = [
    url(r'^create/$', Create.as_view(), name='create'),

    url(r'^$', Moment.as_view(), name='moment'),

    url(r'^comment/$', Comment.as_view(), name='comment')

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
