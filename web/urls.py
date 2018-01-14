#urls

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#view
from .views import WebPage
from .views import Middle

from .views import Post
from .views import Content
from .views import RenderParticipate
from .views import ErrorPage, ContactPage

from .views import WebPageNew

app_name = 'web'

urlpatterns = [
        url(r'^home/$', WebPage.as_view(), name='webpage'),

        url(r'^middle/$', Middle.as_view(), name='middle'),

        url(r'^post/(?P<field>[a-z]+)?/$', Post.as_view(), name='post'),

        url(r'^content/$',Content.as_view(), name='content'),

        url(r'^renderpar/$', RenderParticipate.as_view() , name='ren_par'),

        url(r'^errorpage/$', ErrorPage.as_view(), name="error"),

        url(r'^contactpage/$', ContactPage.as_view(), name="contact"),

        url(r'^homenew/$', WebPageNew.as_view(), name='webpagenew'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
