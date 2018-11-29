from django import forms
from .models import Perrito
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class PerritoForm(forms.ModelForm):

    class Meta:
        model = Perrito
        fields = ('nombre','raza','genero','fecha_ingreso','fecha_nacimiento','imagen','estado','descripcion')
        widgets = {
	        'fecha_ingreso' : DateInput(),
	        'fecha_nacimiento' : DateInput(),
        }