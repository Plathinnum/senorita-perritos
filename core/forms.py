from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('run','nombre','apellido','correo','fecha_nacimiento','telefono','region','comuna','tipovivienda','mensaje',)