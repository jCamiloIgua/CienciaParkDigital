from django.db import models

from django.utils import timezone
# Create your models here.

class Estudiante(models.Model):
    primerNombre = models.CharField(max_length=50)
    segundoNombre = models.CharField(max_length=50)
    primerApellido = models.CharField(max_length=50)
    segundoApellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fechaNacimiento = models.DateField(default=timezone.now)
    edad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nivelEscolar = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)