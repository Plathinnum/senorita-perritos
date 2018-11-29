from django.contrib import admin
from .models import Contacto, Comuna, Region
from adopt.models import Perrito, Estado, Raza

class PerritosAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza','genero','fecha_ingreso','fecha_nacimiento','estado','descripcion')
    search_fields = ('nombre',)
    list_filter = ('raza','genero','estado')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('run','nombre','apellido','correo','fecha_nacimiento','telefono','region','comuna','tipovivienda','mensaje',)
    search_fields = ('run','nombre','apellido')
    list_filter = ('region',)

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Perrito, PerritosAdmin)
admin.site.register(Estado)
admin.site.register(Raza)
admin.site.register(Comuna)
admin.site.register(Region)
