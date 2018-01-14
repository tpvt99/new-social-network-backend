from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist

from user.serialize import serialize_user_basic
from account.models import OnlineTime

def friend_serialize(friend):
    data_serialize = []
    if type(friend) == QuerySet:
        for i in friend:
            try:
                time = i.friend.onlinetime.time
            except ObjectDoesNotExist:
                time = i.friend.last_login
            data = {
                'friend': serialize_user_basic(i.friend),
                'time': time.isoformat()
            }
            data_serialize.append(data)
    else:
        try:
            time = i.friend.onlinetime.time
        except ObjectDoesNotExist:
            time = i.friend.last_login
        data = {
            'friend': serialize_user_basic(friend.friend),
            'time': time.isoformat()
        }
        data_serialize.append(data)
    return data_serialize


def on_friend_serialize(friend):
    data_serialize = []
    if type(friend) == QuerySet:
        for i in friend:
            try:
                time = i.friend.onlinetime.time
            except ObjectDoesNotExist:
                time = i.friend.last_login
            data = {
                'f': i.friend.user_id if type(i.friend.user_id) is str else i.friend.user_id.hex,
                't': time.isoformat()
            }
            data_serialize.append(data)
    else:
        try:
            time = i.friend.onlinetime.time
        except ObjectDoesNotExist:
            time = i.friend.last_login
        data = {
            'f': friend.friend.user_id if type(friend.friend.user_id) is str else friend.friend.user_id.hex,
            't': time.isoformat()
        }
        data_serialize.append(data)
    return data_serialize

def message_serialize(mess):
    data_se = []
    if type(mess) == QuerySet:
        for i in mess:
            data = {
                'message': {
                    'text': i.text
                },
                'us': i.user_send.user_id if type(i.user_send.user_id) is str else i.user_send.user_id.hex,
                'time': i.create_time.isoformat()
            }
            data_se.append(data)
    else:
        data = {
            'message': {
                'text': mess.text
            },
            'us': mess.user_send.user_id if type(mess.user_send.user_id) is str else mess.user_send.user_id.hex,
            'time': mess.create_time.isoformat()
        }
        data_se.append(data)
    return data_se

def pollmessage_serialize(a):
    #a is list of MessageUserInfo
    data = []
    for m in a:
        frame = m.frame
        # saving the fetch
        m.fetch = True
        m.save()
        # done saving the fetch
        user_request_id = m.user.user_id.hex
        users_id = [i.hex for i in list(frame.users.all().values_list('user_id', flat = True))]
        users_id.remove(user_request_id)
        data_se = {
        'target': frame.message_type,
        'total': len(users_id) + 1,
        'allExp': users_id,
        'to': user_request_id,
        'fid': frame.id
        }
        data.append(data_se)
    return data
