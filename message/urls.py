from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from .views import ChatOnline
from .views import ChatFrameInformation
from .views import SendMessage
from .views import GetMessage
from .views import PollMessage

app_name = 'message'

urlpatterns = [

        url(r'^chat/online$', ChatOnline.as_view(), name='ajax'),

        url(r'^chat/frame$', ChatFrameInformation.as_view(), name='frame'),
    
        url(r'^chat/send$', SendMessage.as_view(), name = 'send'),

        url(r'^chat/get_mess', GetMessage.as_view(), name = 'get'),

        url(r'^chat/poll', PollMessage.as_view(), name = 'poll')


        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
