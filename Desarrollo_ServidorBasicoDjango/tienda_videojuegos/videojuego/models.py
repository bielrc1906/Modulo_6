from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.IntegerField()
    plataforma = models.CharField(max_length=50)