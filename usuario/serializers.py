from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Usuario
        fields = [
            "nickname",
            "correo",
            "nombre",
            "apellidos",
        ]
