from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils import request_authentication, request_handler

# Create your views here.
@csrf_exempt
def processRequest(request):
    if request.method == 'POST':
        header = request_authentication.requestHandler(request.headers, request.GET, request.body)
        if header.auth:
            # request_info = request_handler.web_request(request.GET, header.action)
            return HttpResponse(f"Received POST - auth={header.auth} - action={header.action}")
        else:
            return HttpResponse('Received POST')
    if request.method == 'GET':
        print(request)
        return HttpResponse('Received GET')