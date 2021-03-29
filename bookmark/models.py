from django.db import models

# Create your models here.
class Bookmark(models.Model):

    esAnotacion = models.BooleanField()
    cuerpo = models.CharField(max_length=500, blank=True, null=True)
    offset = models.PositiveBigIntegerField()
    titulo = models.CharField(max_length=20)

    Libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
    )

    Usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
    )