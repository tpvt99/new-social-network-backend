from django.db.models.query import QuerySet

from user.serialize import serialize_user_basic

def friend_serialize(friend):
    data_serialize = []
    if type(friend) == QuerySet:
        for i in friend:
            data = {
                'friend': serialize_user_basic(i.friend)
            }
            data_serialize.append(data)
    else:
        data = {
            'friend': serialize_user_basic(friend.friend)
        }
        data_serialize.append(data)
    return data_serialize

