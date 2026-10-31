from django.db import models
from django.core.validators import MinValueValidator

class Pelicula(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Pocas unidades', 'Pocas unidades'),
        ('Agotado', 'Agotado'),
    ]

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    comentarios = models.TextField(blank=True, null=True)

    proveedor = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        help_text="ID del proveedor"
    )
    cantidad = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Disponible'
    )
    precio_renta = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    def __str__(self):
        return self.titulo