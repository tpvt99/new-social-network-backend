from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Fetch, Vote, Comment, PlustagVote, PlustagDelete, FetchProfile

app_name = 'status'

urlpatterns = [
        url(r'^fetch$', Fetch.as_view(), name='content'),

        url(r'^fetch/profile$', FetchProfile.as_view(), name='contentprofile'),

        url(r'^vote/$', Vote.as_view(), name='vote'),

        url(r'^plustag$', PlustagVote.as_view(), name='plustag'),

        url(r'^plustag/delete$', PlustagDelete.as_view(), name='plustag'),

        url(r'^comment$', Comment.as_view(), name='comment')

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
