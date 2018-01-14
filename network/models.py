from django.db import models
from user.models import User
import uuid
from files.models import Image

# Create your models here.
class NetworkAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    network_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
    fullname = models.CharField(max_length = 100)
    birthYear = models.IntegerField()
    #the iso2 code of country
    nationality = models.CharField(max_length = 3)
    sex = models.CharField(max_length = 10)
    profile_picture = models.ForeignKey(Image, on_delete = models.CASCADE)

class NetworkGoal(models.Model):
    user_account = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE)
    goal = models.CharField(max_length = 50)
    select_goal = models.CharField(max_length = 50, null = True)
    introduction = models.TextField()
    time = models.DateTimeField(auto_now_add = True, null = True)

# this model is created for each 2, 3 and more users chatting together, chatroom use this too, it must be unique
class NetworkChatFrame(models.Model):
    users = models.ManyToManyField(NetworkAccount, related_name = "%(app_label)s_%(class)s_user")
    # 2 frame type are goal and room. Goal are for only 2 people and room is for chat room
    frame_type = models.CharField(max_length = 20, default = 'goal')

# this model is used to store more info about each user chatting in a frame, about state of read the message or not, whether user is allowed to do something
class NetworkChatUser(models.Model):
    frame = models.ForeignKey(NetworkChatFrame, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_frame")
    user = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    read = models.BooleanField(default = True)
    fetch = models.BooleanField(default = True)

# this is message 
class NetworkMessage(models.Model):
    user_send = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user_send")
    chat_frame = models.ForeignKey(NetworkChatFrame, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_chat_frame")
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)

# this is info for each message
class NetworkMessageInfo(models.Model):
    user = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    network_message = models.ForeignKey(NetworkMessage, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_network_message")
    read = models.BooleanField(default = False)
    fetch = models.BooleanField(default = False)

class NetworkChatroomTopic(models.Model):
    name = models.CharField(max_length = 100)
    # url is name with space will replace by _
    url = models.CharField(max_length = 100)
    image = models.ForeignKey(Image, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_image", null = True)
    description = models.CharField(max_length = 200, null = True)
    # this use is unneccessary because it will improve and the Admin will edit the topic
    user = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")

class NetworkChatroom(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True)
    tag_topic = models.ManyToManyField(NetworkChatroomTopic, related_name = "%(app_label)s_%(class)s_tag_topic")
    owner = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_owner")

    # this is chat frame using for saving message info for each person
    chat_frame = models.OneToOneField(NetworkChatFrame, on_delete = models.CASCADE, null = True)
    # max people of each chatroom, will be allowed for owner to customized
    max_people = models.IntegerField(default = 5)

# this model is store more info of user in chatroom. The info of user for chatting is stored in model NetworkChatUser
class NetworkChatroomUser(models.Model):
    chatroom = models.ForeignKey(NetworkChatroom, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_chatroom")
    # user and chatroom is unique together
    user = models.ForeignKey(NetworkAccount, on_delete = models.CASCADE, related_name = "%(app_label)s_%(class)s_user")
    #time join
    time_join = models.DateTimeField(auto_now_add = True, null = True)
    # this is used when another user want to chat in your room and you will access or denied
    allow_join = models.BooleanField(default = False)
