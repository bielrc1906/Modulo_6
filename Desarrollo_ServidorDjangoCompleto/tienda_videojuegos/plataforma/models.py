from django.db import models

# Create your models here.

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()