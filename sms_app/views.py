from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json

import requests

from ADS import settings

def send_sms():
    response = requests.get("https://target.t2.ru/api/v2/send_message?operation=send&login=a328d5627d&password=58ac02e411&msisdn=79874353230&shortcode=ADPlatforma&text=test"
    )
    print (response.text)


    
