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
    
class TextSerializer(serializers.Serializer):
    """
    API endpoint
    """
    text=serializers.CharField()
    finalOffset=serializers.IntegerField()
    realCharacters=serializers.IntegerField()