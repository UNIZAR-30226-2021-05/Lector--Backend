from django.db import models

class Usuario(models.Model):
    """
    Usuario del sistema con nickname, password, correo, nombre, apellidos y esAdmin
    """

    # Campos
    nickname = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    esAdmin = models.BooleanField(default=False)



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
    Usuario del sistema con nickname, password, correo, nombre, apellidos y esAdmin
    """

    # Campos
    tamanoLetra = models.PositiveIntegerField()
    nickname = models.CharField(max_length=20, primary_key=True)


    # Métodos
    def __str__(self):
        """
        Cadena para representar el objeto Usuario
        """
        return str(self.tamanoLetra)
