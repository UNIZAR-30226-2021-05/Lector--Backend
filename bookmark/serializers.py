from rest_framework import serializers

from .models import Bookmark


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
        ]