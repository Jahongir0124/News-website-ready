from django import forms
from django.forms import ModelForm
from .models import *
class Form(ModelForm):
    class Meta:
        model=Info
        fields = '__all__'
