from .models import Preferencias
from allauth.account.adapter import DefaultAccountAdapter

class UserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Este método es llamado cuando se registra un usuario mediante allauth.
        Esta redefinición del método permite añadir la configuración del usuario
        registrado.
        """
        user = super(UserAccountAdapter, self).save_user(request, user, form, commit=True)
        pref = Preferencias(usuario=user)
        pref.save()
