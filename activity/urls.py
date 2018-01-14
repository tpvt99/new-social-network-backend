from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'activity'

from .views import CreateActivity
from .views import SearchFilter, Join, ActivityView
from .views import ActivityViewAll, SpecificContent, ActivityPost, ActivityPostComment

urlpatterns = [
    url(r'^create/$', CreateActivity.as_view(), name='create'),

    url(r'^search/$', SearchFilter.as_view(), name='search'),

    url(r'^activity/link/', SpecificContent.as_view(), name='link'),

    url(r'^join/$', Join.as_view(), name='join'),

    url(r'^activitypost/$', ActivityPost.as_view(), name='post'),

    url(r'^activitypost/comment/$', ActivityPostComment.as_view(), name='postcomment'),
    
    url(r'^activity/(?P<id>[0-9]+)?/(?P<head>[\w-]+)?$', ActivityView.as_view(), name = 'activity'),

    url(r'^$', ActivityViewAll.as_view(), name='activityall')

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
