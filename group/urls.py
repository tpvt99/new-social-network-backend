from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import Groups, CreateGroup
from .views import Group, GroupPost, Edit
from .views import Member, Join

app_name = "group"

urlpatterns = [
    url(r'^groups/$', Groups.as_view(),name="groups"),

    url(r'^create/$', CreateGroup.as_view(), name='create'),

    url(r'^member/$', Member.as_view(), name='member'),

    url(r'^join/$', Join.as_view(), name='join'),
    
    url(r'^edit/$', Edit.as_view(), name='edit'),

    url(r'^group/(?P<id>[0-9]+)/$', Group.as_view(), name='group'),

    url(r'^grouppost/$', GroupPost.as_view(), name='grouppost'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
