from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Create, ContestViewAll, ContestView, ContestPost, SearchFilter, Follow

app_name = 'contest'

urlpatterns = [
        url(r'^create/$', Create.as_view(), name='create'),

        url(r'^$', ContestViewAll.as_view(), name='contestall'),
        url(r'^follow/$', Follow.as_view(), name="follow"),

        url(r'^search/$', SearchFilter.as_view(), name='search'),

        url(r'^contestpost/$', ContestPost.as_view(), name='contestpost'),

        url(r'^contest/(?P<id>[0-9]+)/(?P<head>[\w-]+)/?$', ContestView.as_view(), name='contest'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
