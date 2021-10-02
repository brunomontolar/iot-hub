from django.shortcuts import render

from .forms import Device_Actions

def index(request):
    form = Device_Actions
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return render(request, 'controlCenter/index.html', context)
    return render(request, 'controlCenter/index.html', {'form': form})

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")