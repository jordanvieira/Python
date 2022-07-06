from dataclasses import fields
from django.forms import ModelForm
from app.models import Carros


class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['Modelo', 'Marca', 'Ano']
