from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deviceadded', views.deviceAdded, name='deviceAdded'),
    path('addDevice', views.addDevice, name='addDevice'),
    # path('', views.test, name='index'),
]