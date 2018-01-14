SECRET_KEY = 'vn49sdn#$jv%jch'
import uuid
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from user.models import User

def cookie_hash_based_user_uuid(user_uuid):
    if type(user_uuid) is uuid.UUID:
        user_uuid = user_uuid.hex
    st = str.encode(user_uuid + SECRET_KEY)
    return hashlib.md5(st).hexdigest()

def check_cookie_hash_based_user_uuid(user_uuid, cookie):
    hash_cookie = cookie_hash_based_user_uuid(user_uuid)
    if hash_cookie == cookie:
        return True
    return False

def check_authentication(request, is_check_token = True):
    cookie_token = request.COOKIES.get('u')
    user_id = request.COOKIES.get('user')
    user_auto_id = request.COOKIES.get('a')
    if cookie_token and user_id and user_auto_id:
        if check_cookie_hash_based_user_uuid(user_id, cookie_token):
            user = User.objects.get(user_id = user_id, id = user_auto_id)
            if is_check_token:
                au = request.COOKIES.get('au')
                try:
                    if au and user.authentication.token:
                        if au == user.authentication.token:
                            return True
                        return False
                    return False
                except ObjectDoesNotExist:
                    return False
            return True
    return False
