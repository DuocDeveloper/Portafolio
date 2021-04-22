from django.db import models

# Create your models here.
class Subcripcion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    moneda = models.CharField(max_length=255)
    monto = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
