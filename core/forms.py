from django import forms
from .models import Contacto
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('run','nombre','apellido','correo','fecha_nacimiento','telefono','region','comuna','tipovivienda','mensaje',)
        widgets = {
            'fecha_nacimiento': DateInput(),
        }

        