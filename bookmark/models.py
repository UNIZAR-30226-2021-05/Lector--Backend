from django.db import models
import sys
import os.path

#sys.path.append('/home/alonso/Documentos/Uni/3o/cuatri2/PS/Lector--Backend')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from libro.models import Libro
from usuario.models import Usuario

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
    