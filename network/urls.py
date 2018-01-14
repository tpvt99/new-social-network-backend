from django.conf.urls import url
from .views import Register
from .views import Goal
from .views import GetNetwork
from .views import GetNetworkPeople
from .views import GetNetworkFrame
from .views import GetNetworkMessage
from .views import SendNetworkMessage
from .views import PullNetworkMessage
from .views import GetProfileInfo
from .views import SearchTopicChatroom
from .views import TopicChatroom
from .views import ChatroomSettings

app_name = 'network'

urlpatterns = [
    url(r'^network/register', Register.as_view(), name = "register"),

    url(r'^network/profile', GetProfileInfo.as_view(), name = 'profile'),

    url(r'^network/goal', Goal.as_view(), name = "goal"),

    url(r'^network/get', GetNetwork.as_view(), name = "get"),

    url(r'^network/chat/people', GetNetworkPeople.as_view(), name = "people"),

    url(r'^network/chat/frame', GetNetworkFrame.as_view(), name = "frame"),

    url(r'^network/chat/message', GetNetworkMessage.as_view(), name = "fetch"),

    url(r'^network/chat/sendmessage', SendNetworkMessage.as_view(), name = "frame"),

    url(r'^network/chat/pull', PullNetworkMessage.as_view(), name = "pull"),

    url(r'^network/chatroom/search', SearchTopicChatroom.as_view(), name = "search"),

    url(r'^network/chatroom/topic', TopicChatroom.as_view(), name = "topic"),

    url(r'^network/chatroom/settings', ChatroomSettings.as_view(), name = "crc")
]
