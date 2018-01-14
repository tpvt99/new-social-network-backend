from user.serialize import serialize_user_basic

def header_search(user = None):
    data = {}
    data['users'] = []
    if user:
        for i in user:
            data_se = serialize_user_basic(i)
            data['users'].append(data_se)
    return data
