from django.shortcuts import render
from django.http import JsonResponse

# class-based views

from django.views.generic import View

# models

from activity.models import Activity
from user.models import User, Info
from friend.models import Friend
from plan.models import Plan, PlanParticipants, ParticipantMoreInfo
from scholarship.models import Scholarship
from contest.models import Contest


from django.db.models import Q
import ast
import time
from event.models import Event
from django.utils import timezone

# serialize

from search.serialize import header_search
from security.response import set_response_header

# Create your views here.

class HeaderSearch(View):
    def get(self, request):
        # search for user
        q = request.GET.get('q')
        user = User.objects.filter(fullname__icontains = q)[0:10]
        data = {
            'data': header_search(user),
            'status_code': 'ok'
        }
        response = JsonResponse(data)
        set_response_header(response)
        return response
