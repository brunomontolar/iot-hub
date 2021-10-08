from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deviceadded', views.deviceAdded, name='deviceAdded'),
    # path('', views.test, name='index'),
]