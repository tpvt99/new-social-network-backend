from user.serialize import serialize_user_basic

def plustag_serialize(plustag):
    return {
        'id': plustag.pk,
        'user_receiver_plus': serialize_user_basic(plustag.user_receive_plus) if plustag.user_receive_plus else None,
        'user_send_plus': serialize_user_basic(plustag.user_send_plus) if plustag.user_send_plus else None,
        'status': plustag.status.id if plustag.status else None,
        'plustag_name': plustag.plustag_name,
        'votes': plustag.votes,
        'create_time': plustag.create_time.isoformat(),
        'uservotes': plustag_vote_serialize(plustag)
        }

def plustag_status_serialize(plustag):
    return {
        'id': plustag.pk,
        'user_send_plus': serialize_user_basic(plustag.user_send_plus) if plustag.user_send_plus else None,
        'status': plustag.status.id if plustag.status else None,
        'plustag_name': plustag.plustag_name,
        'votes': plustag.votes,
        'create_time': plustag.create_time.isoformat(),
        'uservotes': plustag_vote_serialize(plustag)
        }

def plustag_vote_serialize(plustag):
    pv = plustag.plustag_plustagvote_plustag.filter(been_vote = True)
    data = []
    for i in pv:
        data.append({
            'user_vote': serialize_user_basic(i.user_vote),
            'been_vote': i.been_vote,
            'time': i.time.isoformat()
            })
    return data
