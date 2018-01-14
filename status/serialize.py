from post.serialize import serialize_post
from user.serialize import serialize_user_basic
from plustag.serialize import plustag_serialize, plustag_status_serialize
from status.models import Status, StatusVote
from django.db.models.query import QuerySet

# VOTE

def status_vote_serialize(status):
    sv = status.status_statusvote_status.all()
    data_se = []
    for i in sv:
        if i.been_vote == True:
            data_se.append({
                'user': serialize_user_basic(i.user)
                })
    return data_se

def status_user_vote_serialize(status, user):
    try:
        sv = StatusVote.objects.get(status = status, user = user)
    except StatusVote.DoesNotExist:
        return {
                'been_vote': False,
            }
    return {
        'been_vote': sv.been_vote,
        }


# COMMENT

def status_comment_serialize(status, number_query = 3, page = 0):
    data = []
    sc = status.status_statuscomment_status.all().order_by('-time_create')[page:page+number_query]
    for i in sc:
        obj = {
                'user': serialize_user_basic(i.user),
                'id': i.pk,
                'comment': i.comment,
                'time': i.time_create.isoformat()
            }
        data.append(obj)
    return data


# PLUSTAG

def status_plustag_serialize(status):
    pt = status.plustag_plustag_status.all().order_by('-create_time')
    data_serialize = []
    for i in pt:
        data_serialize.append(plustag_status_serialize(i))
    return data_serialize

# REACTION

def status_reaction_user_vote_serialize(statusreaction):
    sv = statusreaction.status_statusreactionvote_statusreaction.filter(been_vote = True)
    data = []
    for i in sv:
        data_se = {
                'user': serialize_user_basic(i.user)
            }
        data.append(data_se)
    return data

def status_reaction_serialize(status, user = None):
    data = []
    sr = status.status_statusreaction_status.all()
    for i in sr:
        data_se = {
            'statusId': i.status.pk,
            'reactionId': i.pk,
            'reactionName': i.reactionName,
            'reactionType': i.reactionType,
            'votes': i.vote,
            'userVotes': status_reaction_user_vote_serialize(i)
        }
        data.append(data_se)
    return data

def status_serialize(status, user = None):
    data_serialize = []
    if type(status) == QuerySet:
        for i in status:
            data_in = {
                'id': i.id,
                'type': i.verb,
                'votes': i.vote,
                'user': serialize_user_basic(i.user),
                'post': serialize_post(i.post),
                'time': i.time_create.isoformat(),
                'totalComments': len(i.status_statuscomment_status.all()),
                'comments': status_comment_serialize(i, 3),
                'plustags': status_plustag_serialize(i),
                'reactions': status_reaction_serialize(i, user),
                'df_r': i.use_default_reaction,
                'ct_r': i.use_custom_reaction
                }
            data_serialize.append(data_in)
    else:
        data_in = {
            'id': status.id,
            'type': status.verb,
            'votes': status.vote,
            'user': serialize_user_basic(status.user),
            'post': serialize_post(status.post),
            'time': status.time_create.isoformat(),
            'totalComments': len(status.status_statuscomment_status.all()),
            'comments': status_comment_serialize(status, 3),
            'plustags': status_plustag_serialize(status),
            'reactions': status_reaction_serialize(status, user),
            'df_r': status.use_default_reaction,
            'ct_r': status.use_custom_reaction
            }
        data_serialize.append(data_in)
    return data_serialize
