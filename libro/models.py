from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return str(self.nombre)


# Create your models here.
class Libro(models.Model):
    """
    Modelo de libro, con ISBN, path, titulo, path a portada, sinopsis, formato
    """

    # Campos
    ISBN = models.CharField(max_length=13, primary_key=True)
    pathLibro = models.CharField(max_length=200)
    titulo = models.CharField(max_length=30)
    portada = models.CharField(max_length=200 , blank=True)
    sinopsis = models.CharField(max_length=1000, blank=True)
    formato = models.CharField(max_length=5)
    
    autor = models.ForeignKey(
        Autor,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    # Métodos

class Genero(models.Model):
    genero = models.CharField(max_length=15, primary_key=True)

    Libro = models.ManyToManyField(
        Libro,
        blank=True
    )

    def __str__(self):
        return str(self.genero)



