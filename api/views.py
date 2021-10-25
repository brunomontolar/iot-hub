from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils import request_authentication
# Create your views here.
@csrf_exempt
def processRequest(request):
    if request.method == 'POST':
        header = request_authentication.requestAuthentication(request.headers)
        if header.auth:
            print(request)
            print(request.body)
            return HttpResponse(f"Received POST - auth={header.auth} - action={header.action}")
        else:
            return HttpResponse('Received POST')
    if request.method == 'GET':
        print(request)
        return HttpResponse('Received GET')