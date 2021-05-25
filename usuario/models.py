from django.db import models
from django.contrib.auth.models import AbstractUser
import sys
import os.path

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from libro.models import Libro



class Usuario(AbstractUser):
    """
    Modelo usuario que hereda del usuario Django los atributos:
    id           | integer                  |           | not null | nextval('usuario_usuario_id_seq'::regclass)
    password     | character varying(128)   |           | not null | 
    last_login   | timestamp with time zone |           |          | 
    is_superuser | boolean                  |           | not null | 
    username     | character varying(150)   |           | not null | 
    first_name   | character varying(150)   |           | not null | 
    last_name    | character varying(150)   |           | not null | 
    email        | character varying(254)   |           | not null | 
    is_staff     | boolean                  |           | not null | 
    is_active    | boolean                  |           | not null | 
    date_joined  | timestamp with time zone |           | not null | 

    """
    pathFoto = models.CharField(max_length=150, default="url de foto no especificada")

    Libro = models.ManyToManyField(
        Libro,
        blank=True,
        through="Guardar"
    )

    # Métodos
    """
        def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
    """ 
    def __str__(self):
        """
        Cadena para representar el objeto Usuario
        """
        return self.username


class Guardar(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntuacion = models.PositiveIntegerField(default=0)
    currentOffset = models.PositiveIntegerField(default=0)
    leyendo = models.BooleanField(default=False)




class Preferencias(models.Model):
    """
    Modelo de configuracion, con tamanoLetra, tipoLetra, colorBg y colorLetra
    """

    # Campos
    tamanoLetra = models.PositiveIntegerField(default=12)
    tipoLetra = models.CharField(max_length=50, default='arial')
    colorBg = models.CharField(max_length=50, default='white')
    colorLetra = models.CharField(max_length=50, default='black')
 
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1
    )

    # Métodos
    def __str__(self):
        """
        Cadena para representar el objeto Usuario
        """
        return str(self.usuario.username)

class Coleccion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, default='tituloColeccion')

    class Meta:
        unique_together = ('usuario', 'titulo')

class Agrupar(models.Model):
        coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
        libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

        class Meta:
            unique_together = ('coleccion', 'libro')