from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def processRequest(request):
    if request.method == 'POST':
        return HttpResponse('Received POST')
    if request.method == 'GET':
        #print(request)
        return HttpResponse('Received GET')