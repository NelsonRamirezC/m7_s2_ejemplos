from django.forms import ModelForm
from django import forms

from .models import Perfil

class PerfilFormUpdate(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'biografia', 
            'celular',
        ]
         
        widgets = {
            "biografia": forms.Textarea(attrs={"class": 'form-control', "rows": 3}),
            "celular": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 13}),
        }
