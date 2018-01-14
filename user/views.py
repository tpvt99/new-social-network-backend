from django.shortcuts import render
from django.views.generic import View
import uuid
import hashlib
from .models import User
from .models import Info
from django.http import JsonResponse
SECRET_KEY = 'vn49sdn#$jv%jch'
from security.response import set_response_header
from account.serialize import newfeed_serialize
from account.method import set_online_time

# Create your views here.

def cookie_hash(user_id):
    if type(user_id) is uuid.UUID:
        user_id = user_id.hex
    st = str.encode(user_id + SECRET_KEY)
    return hashlib.md5(st).hexdigest()

def check_cookie_hash(user_id, cookie):
    hash_cookie = cookie_hash(user_id)
    if hash_cookie == cookie:
        return True
    return False

class Authentication(View):
    def get(self, request):
        cookie_token = request.COOKIES.get('u')
        user_id = request.COOKIES.get('user')
        user_auto_id = request.COOKIES.get('a')
        if cookie_token and user_id and user_auto_id:
            if check_cookie_hash(user_id, cookie_token):
                user = User.objects.get(user_id = user_id,id = user_auto_id)
                info = Info.objects.get(user = user)
                data_response = {
                    'status': 'ok',
                    'user': {
                        'user_id': user.user_id.hex,
                        'email': user.email,
                        'fullname': user.fullname,
                        'profilepic': info.profile_pic.url if info.profile_pic else '',
                        'backgroundpic': info.background_pic.url if info.background_pic else '',
                        'newfeed': newfeed_serialize(user)
                    }
                }
                set_online_time(user)
                response = JsonResponse(data_response)
                set_response_header(response) 
                return response
        response = JsonResponse({'status':'no'})
        set_response_header(response)
        return response
