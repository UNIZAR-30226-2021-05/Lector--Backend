from rest_framework import serializers

from .models import Bookmark, Usuario


class BookmarkSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Bookmark
        fields = [
            "esAnotacion",
            "cuerpo",
            "offset",
            "titulo",
            "Libro",
            "Usuario",
            "id",
        ]

class UsuarioIDSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Usuario
        fields = [
            "id",
        ]