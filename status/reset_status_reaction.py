# this script will move default vote from status to status reaction

from status.models import Status
from status.models import StatusReaction
from status.models import StatusReactionVote

def reset(status):
    for i in status:
        status_reaction = i.status_statusreaction_status.all()
        if len(status_reaction) > 0:
            pass
        else:
            status_reaction = StatusReaction.objects.create(status = i, reactionName = 'like', reactionType = '1', icon = 'heart')
            status_reaction.vote = i.vote
            status_reaction.save()
            status_vote = i.status_statusvote_status.all()
            for a in status_vote:
                StatusReactionVote.objects.create(statusreaction = status_reaction, user = a.user, been_vote = a.been_vote, time_create = a.time_create)
