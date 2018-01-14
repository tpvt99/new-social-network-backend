from django.db.models.query import QuerySet
from user.serialize import serialize_user_basic

def notification_serialize(notification):
    data = []
    if type(notification) == QuerySet:
        for i in notification:
           data_se = {
                'noti_type': i.noti_type,
                'time': i.time.isoformat(),
                'data': noti_content_serialize(i)
            }
           data.append(data_se)
    else:
       data_se = {
            'noti_type': notification.noti_type,
            'time': notification.time.isoformat(),
            'data': noti_content_serialize(notification)
        }
       data.append(data_se)
    return data

#status A Notification

def status_A_serialize(noti):
    status_a_notification = noti.noti_statusanotification_noti
    return {
        'status': status_a_notification.status.id,
        'user': serialize_user_basic(status_a_notification.user)
    }

# status B Notification

def reset_B(status_b_notification):
    if status_b_notification.user is None:
        status_b_notification.user = status_b_notification.statuscomment.user

def status_B_serialize(noti):
    status_b_notification = noti.noti_statusbnotification_noti
    reset_B(status_b_notification)
    return {
        'status': status_b_notification.status.id,
        'user': serialize_user_basic(status_b_notification.user),
        'statuscomment': status_b_notification.statuscomment.id,
        'comment': status_b_notification.statuscomment.comment
    }

def noti_content_serialize(noti):
    data = ''
    if noti.noti_type == 'status-a':
        data = status_A_serialize(noti)
    elif noti.noti_type == 'status-b':
        data = status_B_serialize(noti)
    return data
