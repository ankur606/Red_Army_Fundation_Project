from dataclasses import field, fields
from django import forms
from .models import *

class EventsForm(forms.ModelForm):
    class Meta:
        model = EventsModel
        fields = ['image', 'headding']