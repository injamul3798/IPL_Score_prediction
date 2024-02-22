from django import forms
from .models import Model

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'
