from django import forms
from django.forms import ModelForm
from .models import data
class dataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = '__all__'