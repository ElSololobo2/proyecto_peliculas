from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo