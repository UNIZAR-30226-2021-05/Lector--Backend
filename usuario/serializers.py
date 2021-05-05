from rest_framework import serializers

from .models import Usuario, Preferencias


class UsuarioSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "pathFoto",
            "id",
        ]

class PreferenciasSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Preferencias
        fields = [
            "tamanoLetra",
            "tipoLetra",
            "colorBg",
            "colorLetra",
        ]
