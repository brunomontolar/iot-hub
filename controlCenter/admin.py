from django.contrib import admin
from .models import Devices, Actions

admin.site.register(Devices, Actions)