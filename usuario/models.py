from django.db import models
from django.contrib.auth.models import AbstractUser


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



    # Métodos
    '''def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
       ''' 
    def __str__(self):
        """
        Cadena para representar el objeto Usuario
        """
        return self.nickname

class Configuracion(models.Model):
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
        return str(self.tamanoLetra)
