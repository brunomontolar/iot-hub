from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Devices, Actions
from .forms import ActionsForm, Device_Actions, DevicesForm

def index(request):
    form = DevicesForm(request.POST or None)
    form2 = ActionsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        if form2.is_valid():
            form2.save()
    devices = Devices.objects.all()
    actions = Actions.objects.all()
    
    #     form = DevicesForm(request.POST)
    #     form2 = ActionsForm(request.POST)
        # if form.is_valid():
        #     return HttpResponseRedirect('/thanks')
    # else:
    #     form = DevicesForm
    #     form2 = ActionsForm
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return render(request, 'controlCenter/index.html', context)
    return render(request, 'controlCenter/index.html', {'form': form, 'form2': form2, 'devices': devices, 'actions': actions})

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def deviceAdded(request):
    if request.method == 'POST':
        form = DevicesForm(request.POST)
        # if form.is_valid():
        #     return HttpResponseRedirect('/thanks')
    else:
        form = DevicesForm
    form2 = ActionsForm
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return render(request, 'controlCenter/index.html', context)
    return render(request, 'controlCenter/index.html', {'form': form, 'form2':form2})

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")