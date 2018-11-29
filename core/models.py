from django.db import models
from django.utils import timezone

tipo_vivienda = (
	('Patio grande','Patio grande'),
	('Patio pequeño','Patio pequeño'),
	('Casa sin patio','Casa sin patio'),
	('Departamento','Departamento'),
)

class Region(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

class Comuna(models.Model):
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Contacto(models.Model):
	run = models.CharField(primary_key=True, max_length=50)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	fecha_nacimiento = models.DateField(blank=True, null=False)
	telefono = models.CharField(max_length=50)
	region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
	comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
	tipovivienda = models.CharField(max_length=30, choices=tipo_vivienda)
	mensaje = models.TextField(max_length=50)
	
	def publish(self):
		self.save()
	
	def __str__(self):
		return self.run
