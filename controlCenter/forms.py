from django import forms
from django.forms import ModelForm
from .models import Devices, Actions

from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget

class Device_Actions(forms.Form):
    device_name = forms.CharField(label='Device name', max_length=100)
    input_status = forms.BooleanField(label='Status')

class DevicesForm(ModelForm):
    
    class Meta:
        model = Devices
        fields = ['device', 'startup_date']
        labels = {
            'device': (''),
            'startup_date': (''),
        }
        widgets = {
            'device' : forms.TextInput(attrs = {'placeholder': 'Dispositivo'}),
            'startup_date' : forms.TextInput(attrs = {'placeholder': 'Data'}),
        }

class ActionsForm(ModelForm):
    class Meta:
        model = Actions 
        fields = ['device_id', 'input_name', 'input_value', 'input_type']