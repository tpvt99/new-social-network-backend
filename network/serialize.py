from user.serialize import serialize_user_basic
from files.serialize import serialize_image
from django.db.models.query import QuerySet

def network_account_serialize(account):
    data = {
    'network_id': account.network_id.hex,
    'fullname': account.fullname,
    'birthYear': account.birthYear,
    'nationality': account.nationality,
    'sex': account.sex,
    'profile_picture': serialize_image(account.profile_picture)
    }
    return data

def network_account_moreinfo_serialize(account):
    data = {
    }
    return data

def network_goal_serialize(goals):
    data_se = []
    if type(goals) == QuerySet:
        for i in goals:
            data = {
            'goal': i.goal,
            'select_goal': i.select_goal,
            'introduction': i.introduction
            }
            data_se.append(data)
    else:
        data = {
        'goal': goals.goal,
        'select_goal': goals.select_goal,
        'introduction': goals.introduction
        }
        data_se.append(data)
    return data_se

def network_serialize(goals, tab_section= None):
    if tab_section:
        data = {
        'name': tab_section,
        'data': []
        }
        if type(goals) == QuerySet:
            for i in goals:
                data_se = {
                'user': network_account_serialize(i.user_account),
                'goal': network_goal_serialize(i)
                }
                data['data'].append(data_se)
        else:
            data_se = {
            'user': network_account_serialize(goals.user_account),
            'goal': network_goal_serialize(goals)
            }
            data['data'].append(data_se)
        return data
    return False
# this is each message in messages
def network_message_serialize(messages):
    data_se = []
    if type(messages) == QuerySet:
        for i in messages:
            data = {
            'us': i.user_send.network_id.hex,
            'message': {
                'text': i.text
            },
            'time': i.create_time.isoformat()
            }
            data_se.append(data)
    else:
        data = {
        'us': messages.user_send.network_id.hex,
        'message': {
            'text': messages.text
        },
        'time': messages.create_time.isoformat()
        }
        data_se.append(data)
    return data_se

def network_chat_frame_serialize(frame, fetch_message = False):
    data = {
    'frame_id': frame.id,
    'users': []
    }
    for i in frame.users.all():
        data['users'].append(network_account_serialize(i))
    return data

def pull_message_serialize(frame_user_info):
    # frame_user_info is a list of NetworkChatFrame
    data = []
    for i in frame_user_info:
        data_se = {
        'frame_id': i.frame.id
        }
        data.append(data_se)
    return data

def topic_serialize(topic):
    data = []
    if type(topic) == QuerySet:
        for i in topic:
            data_se = {
            'id': i.id,
            'name': i.name,
            'url': i.url,
            'image': serialize_image(i.image),
            'description': i.description
            }
            data.append(data_se)
    else:
        i = topic
        data_se = {
        'id': i.id,
        'name': i.name,
        'url': i.url,
        'image': serialize_image(i.image),
        'description': i.description
        }
        data.append(data_se)
    return data

# this is helper fufnction for network_chatroom_serialize which receive network_chatroom and returns all topics that this chatroom has tagged in

def network_chatroom_topics_serialize(network_chatroom):
    data = []
    topics = network_chatroom.tag_topic.all()
    for i in topics:
        data_se = {
        'name': i.name,
        'url': i.url,
        'image': '',
        'description': i.description
        }
        data.append(data_se)
    return data

# this is helper function for network_chatroom_serialize which recieve network_chatroom and returns data of all users in this chatroom
def network_chatroom_users_serialize(network_chatroom):
    data = []
    users = network_chatroom.network_networkchatroomuser_chatroom.filter(allow_join = True)
    for i in users:
        data_se = network_account_serialize(i.user)
        data.append(data_se)
    return data
# this is helper function for network_chatroom_serialize which recieve network_chatroom and returns data of users is wating to accept to join in this chatroom
def network_chatroom_users_pending_serialize(network_chatroom):
    data = []
    users = network_chatroom.network_networkchatroomuser_chatroom.filter(allow_join = 
False)
    for i in users:
        data_se = network_account_serialize(i.user)
        data.append(data_se)
    return data
# this serialize function returns data of chatroom, network_chatrooms is list of chatroom
def network_chatroom_serialize(network_chatrooms):
    data_se = []
    if type(network_chatrooms) == QuerySet:
        for i in network_chatrooms:
            data = {
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'owner': network_account_serialize(i.owner),
            'frame_id': i.chat_frame.id,
            'max_people': i.max_people,
            'users': network_chatroom_users_serialize(i),
            'users_pending': network_chatroom_users_pending_serialize(i),
            'topics': network_chatroom_topics_serialize(i)
            }
            data_se.append(data)
    else:
        i = network_chatrooms
        data = {
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'owner': network_account_serialize(i.owner),
        'frame_id': i.chat_frame.id,
        'max_people': i.max_people,
        'users': network_chatroom_users_serialize(i),
        'users_pending': network_chatroom_users_pending_serialize(i),
        'topics': network_chatroom_topics_serialize(i)
        }
        data_se.append(data)
    return data_se
