from django.db import models

# Create your models here.
class Libro(models.Model):
    """
    Modelo de libro, con ISBN, path, titulo, path a portada, sinopsis, formato, ¿¿puntuacion??
    """

    # Campos
    ISBN = models.PositiveBigIntegerField(primary_key=True)
    pathLibro = models.FileField(upload_to='libros/')
    titulo = models.CharField(max_length=30)
    portada = models.FileField(upload_to='portadas/', blank=True)
    sinopsis = models.CharField(max_length=1000, blank=True)
    formato = models.CharField(max_length=5)
    
    """
    Autor = models.ForeignKey(
        Autor,
        default = 'Desconocido'
    )
    Genero = models.ManyToManyField(
        Genero,
        default = 'Sin determinar'
    )
    """
    
    # Métodos
"""
class Autor(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)

    Libro = models.ForeignKey(
        Libro
    )

    def __str__(self):
        return str(self.nombre)

class Genero(models.Model):
    genero = models.CharField(max_length=15, primary_key=True)

    Libro = models.ManyToManyField(
        Libro
    )

    def __str__(self):
        return str(self.genero)
"""