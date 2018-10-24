from django import forms
from .models import Perrito

class PerritoForm(forms.ModelForm):

    class Meta:
        model = Perrito
        fields = ('nombre','raza','genero','fecha_ingreso','fecha_nacimiento','imagen','estado',)