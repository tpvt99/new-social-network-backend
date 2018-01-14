from .models import User, Info, Account
from django.core.exceptions import ObjectDoesNotExist
import re
from account.serialize import newfeed_serialize


def reset(user):
    pat = re.compile(r'\W+')
    try:
        account = user.account
        account.profilename = re.sub(pat, '_', account.profilename)
        account.save()
    except ObjectDoesNotExist:
        account = Account.objects.create(user = user, profilename = re.sub(pat, '_', user.email.split('@')[0]))
    try:
        info = user.info
    except ObjectDoesNotExist:
        info = Info.objects.create(user = user)

def serialize_user_basic(user):
    reset(user)
    return {
        'id': user.user_id if type(user.user_id) is str else user.user_id.hex,
        'email': user.email,
        'fullname': user.fullname,
        'profileimage': user.info.profile_pic.url if user.info.profile_pic else '',
        'backgroundimage': user.info.background_pic.url if user.info.background_pic else '',
        'profileUrl': user.account.profilename
        }
