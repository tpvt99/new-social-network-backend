from user.serialize import serialize_user_basic


def total_friends(user):
    friend = user.friend_friend_user.all()
    return len(friend)

def friend_info(user, number_friends = 10):
    friend = user.friend_friend_user.all()[0:number_friends]
    data = []
    for i in friend:
        data.append(serialize_user_basic(i.friend))
    return data

def basic_info(user):
   data = {
    'total_friends': total_friends(user),
    'friends': friend_info(user, 6)
   }
   return data
