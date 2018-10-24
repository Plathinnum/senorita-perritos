from django.db import models
from django.utils import timezone

tipo_vivienda = (
	('Patio grande','Patio grande'),
	('Patio pequeño','Patio pequeño'),
	('Casa sin patio','Casa sin patio'),
	('Departamento','Departamento'),
	)
comuna = (
	('Arica','Arica'),

)
region = (
	('Arica y Parinacota','Arica y Parinacota'),

)


class Contacto(models.Model):
	run = models.CharField(primary_key=True, max_length=50)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	fecha_nacimiento = models.DateTimeField(blank=True, null=False)
	telefono = models.IntegerField()
	region = models.CharField(max_length=30, choices=region)
	comuna = models.CharField(max_length=30, choices=comuna)
	tipovivienda = models.CharField(max_length=30, choices=tipo_vivienda)
	mensaje = models.TextField(max_length=50)
	
	def publish(self):
		self.save()
	
	def __str__(self):
		return self.run