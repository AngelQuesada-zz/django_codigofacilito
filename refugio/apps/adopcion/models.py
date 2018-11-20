from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField(max_length=254)
    domicilio = models.TextField()

