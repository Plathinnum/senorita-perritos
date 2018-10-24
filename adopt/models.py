from django.db import models
from django.utils import timezone
import os

genero = (
    ('H','Hembra'),
    ('M','Macho'),
    )

	
	
class Raza (models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
	
class Estado (models.Model):
    nombre = models.CharField(max_length=50)
	
    def __str__(self):
        return self.nombre
	
class Perrito(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.CharField(max_length=30, choices=genero)
    fecha_ingreso = models.DateTimeField(blank=True, null=False)
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    imagen = models.ImageField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	

    def publish(self):
        return self.save()
	
    def __str__(self):
        return self.nombre
