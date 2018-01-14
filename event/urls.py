from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import CreateEvent, EventViewAll,EventView, SearchFilter, Join, SpecificContent, EventPost, EventPostComment
app_name = 'event'

urlpatterns = [
        url(r'^create/$', CreateEvent.as_view(), name='create'),

        url(r'^event/(?P<id>[0-9]+)/(?P<head>[\w-]+)/?$', EventView.as_view(), name="event"),

        url(r'^event/link/', SpecificContent.as_view(), name='link'),

        url(r'^$', EventViewAll.as_view(), name='eventall'),

        url(r'^eventpost/$',EventPost.as_view(), name='post'),
        url(r'^eventpost/comment/$', EventPostComment.as_view(), name='postcomment'),
        
        url(r'^search/$', SearchFilter.as_view(), name='searchfilter'),

        url(r'^join/$', Join.as_view(), name='join'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
