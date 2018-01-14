from django.shortcuts import render
from django.views.generic import View
from .models import Notification
import time
from django.http import JsonResponse

from security.response import set_response_header
from authentication.auth import check_authentication
from user.method import get_user
from .serialize import notification_serialize

# Create your views here.

class FetchNoti(View):
    def get(self, request):
        if check_authentication(request):
            user = get_user(request)
            try:
                currentIndex = int(request.GET.get('currentIndex'))
            except ValueError:
                currentIndex = 0
            noti_type = ['status-a','status-b']
            notis = Notification.objects.filter(user = user, noti_type__in = noti_type).order_by('-time')[currentIndex:currentIndex+10]
            unread_noti = len(Notification.objects.filter(user = user, read = False, noti_type__in = noti_type))
            data = {
                'data': notification_serialize(notis),
                'unread': unread_noti,
                'status_code': 'ok'
                }
            response = JsonResponse(data)
            set_response_header(response)
            return response
        else:
            data = {
            'status_code': 'error'
            }
            response = JsonResponse(data)
            set_response_header(response)
            return response
