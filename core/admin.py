from django.contrib import admin
from .models import Contacto
from adopt.models import Perrito, Estado, Raza

admin.site.register(Contacto)
admin.site.register(Perrito)
admin.site.register(Estado)
admin.site.register(Raza)