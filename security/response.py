from django.http import HttpResponse
import json

AccessControlAllowOrigin = 'http://127.0.0.1:8080'

def set_response_header(response):
    response['Access-Control-Allow-Origin'] = AccessControlAllowOrigin
    response['Access-Control-Allow-Credentials'] = 'true'

def response_error():
    data = {
    'status_code': 'error'
    }
    response = HttpResponse('while(1);'+json.dumps(data), content_type = 'text/javascript')
    return response
