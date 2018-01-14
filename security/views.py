from django.shortcuts import render
from django.http import HttpResponse
import json

from django.views.generic import View
from django.middleware import csrf

from .response import set_response_header
from authentication.auth import check_authentication
from user.method import get_user
from user.serialize import serialize_user_basic
from network.models import NetworkAccount
from network.serialize import network_account_serialize

# Create your views here.

class CsrfToken(View):
    def get(self, request):
        token = csrf.get_token(request)
        response = HttpResponse('', content_type = 'application/x-javascript; charset=utf-8')
        response.set_cookie(key = 'csrftoken', value = token, max_age = 60*60*24)
        set_response_header(response)
        return response

class CheckAuthentication(View):
    def get(self, request):
        if check_authentication(request, True):
            user = get_user(request)
            data = {
            'status_code': 'ok',
            'user': serialize_user_basic(user)
            }
            response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
            set_response_header(response)
            return response
        data = {
            'status_code': 'error'
        }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8')
        set_response_header(response)
        return response

class CheckNetworkAuthentication(View):
    def get(self, request):
        if check_authentication(request, True):
            user = get_user(request)
            try:
                network_account = NetworkAccount.objects.get(user = user)
                data = {
                'data':network_account_serialize(network_account),
                'status_code': 'ok'
                }
                response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8;')
                set_response_header(response)
                response.set_cookie(key = 'nu', value = network_account.network_id.hex, max_age = 60*60*24)
                return response
            except NetworkAccount.DoesNotExist:
                pass
        data = {
        'status_code': 'error'
        }
        response = HttpResponse('while(1);' + json.dumps(data), content_type = 'application/x-javascript; charset=utf-8;')
        set_response_header(response)
        return response
