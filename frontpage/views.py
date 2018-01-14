# response

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

# class-based view

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
import datetime

# settings

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
from django.core.exceptions import ObjectDoesNotExist
import uuid
from django.db.utils import IntegrityError
import hashlib

# models

from user.models import MyUser, Info, Authentication
from user.models import User
import re

from user.views import SECRET_KEY
from security.response import set_response_header
from authentication.auth import check_authentication
from account.method import set_online_time

# Create your views here.


class Helper(View):
    def validateEmail(self, email):
        t = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if t.match(email) and t.match(email).group() == email:
            return True
        return False

    def validateName(self, name):
        z = name.split(' ')
        for i in z:
            if not i.isalpha() and i != '':
                return False
        return True

    def token_auth_generate(self):
        return uuid.uuid4().hex

    def cookie_hash(self, user_id):
        if type(user_id) is uuid.UUID:
            user_id = user_id.hex
        st = str.encode(user_id + SECRET_KEY)
        return hashlib.md5(st).hexdigest()

    def check_cookie_hash(self, user_id, cookie):
        hash_cookie = self.cookie_hash(user_id)
        if hash_cookie == cookie:
            return True
        return False

class Register(Helper):
    def post(self, request):
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            fullname = fullname.strip()
            password = password.strip()
            email = email.strip()
        except:
            response = JsonResponse({'status':'error'})
            set_response_header(response)
            return response
        if len(password) < 6:
            response = JsonResponse({'status':'password'})
            set_response_header(response)
            return response
        if not self.validateEmail(email):
            response = JsonResponse({'status':'email'})
            set_response_header(response)
            return response
        if not self.validateName(fullname):
            response = JsonResponse({'status':'fullname'})
            set_response_header(response)
            return response
        try:
            MyUser.objects.get(email = email.strip())
            response = JsonResponse({'status':'fullname'})
            set_response_header(response)
            return response
        except MyUser.DoesNotExist:
            x = MyUser.objects.create_user(
                            email = email,
                            fullname = fullname,
                            password = password)
            user = User.objects.create(id=x.id, email = email, password = x.password, fullname = fullname)
            info = Info.objects.create(user = user)
            response = JsonResponse({'status':'ok'})
            response.set_cookie(key = 'u', value = self.cookie_hash(user.user_id), max_age = 60*60*24)
            if type(user.user_id) is uuid.UUID:
                response.set_cookie(key = 'user', value = user.user_id.hex, max_age = 60*60*24)
            else:
                response.set_cookie(key = 'user', value = user.user_id, max_age = 60*60*24)
            response.set_cookie(key = 'a', value = user.id, max_age = 60*60*24)
            # generate token authentication
            token = uuid.uuid4().hex
            try:
                Authentication.objects.create(user = user, token = token)
            except IntegrityError:
                user.authentication.token = token
                user.authentication.save()
            response.set_cookie(key = 'au', value = token, max_age = 60*60*24)
            set_response_header(response)
            return response

class Login(Helper):
    def options(self, request):
        response = HttpResponse()
        response['Access-Control-Allow-Method'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'X-Requested-With, x-csrftoken'
        response['Access-Control-Allow-Origin'] = AccessControlAllowOrigin
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Max-Age'] = '1800'
        return response

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        x = authenticate(email = email, password = password)
        if x is not None:
            try:
                user = User.objects.get(id=x.id)
                user.last_login = timezone.now()
                user.save()
            except User.DoesNotExist:
                user = User.objects.create(id = x.id, email = email, password = x.password, fullname = x.fullname)
            response = JsonResponse({'status_code':200})
            response.set_cookie(key = 'u', value = self.cookie_hash(user.user_id), max_age = 60*60*24)
            if type(user.user_id) is uuid.UUID:
                response.set_cookie(key = 'user', value = user.user_id.hex, max_age = 60*60*24)
            else:
                response.set_cookie(key = 'user', value = user.user_id, max_age = 60*60*24)
            response.set_cookie(key = 'a', value = user.id, max_age = 60*60*24)
            token = uuid.uuid4().hex
            try:
                Authentication.objects.create(user = user, token = token)
            except IntegrityError:
                au = Authentication.objects.get(user = user)
                au.token = token
                au.save()
            response.set_cookie(key = 'au', value = token, max_age = 60*60*24)
            set_response_header(response)
            return response
        response = JsonResponse({'status_code':401})
        set_response_header(response)
        return response

class Logout(View):
    def post(self, request):
        response = JsonResponse({'status_code':'ok'})
        response.delete_cookie('a')
        response.delete_cookie('user')
        response.delete_cookie('u')
        response.delete_cookie('au')
        set_response_header(response)
        return response
