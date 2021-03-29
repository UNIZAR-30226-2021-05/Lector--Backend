from rest_framework import serializers

from .models import Libro


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
        ]