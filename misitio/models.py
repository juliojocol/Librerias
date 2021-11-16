from django.db import models
from django.utils import timezone

# Create your models here.
class Publicacion(models.Model):
    producto = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.CharField(max_length=200)

    def __str__(self):
       return self.producto

    class Meta:
        verbose_name_plural = 'Publicaciones'
