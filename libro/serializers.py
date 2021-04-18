from rest_framework import serializers

from .models import *


class LibroSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Libro
        fields = [
            "ISBN",
            "pathLibro",
            "portada",
            "formato",
            "titulo",
            "sinopsis",
            "autor",
        ]

class AutorSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Autor
        fields = [
            "nombre",
        ]

class GeneroSerializer(serializers.ModelSerializer):
    """
    API endpoint
    """

    class Meta:
        model = Genero
        fields = [
            "genero",
            "Libro",
        ]