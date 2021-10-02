from django import forms

from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget

class Device_Actions(forms.Form):
    device_name = forms.CharField(label='Device name', max_length=100)
    input_status = forms.BooleanField(label='Status')