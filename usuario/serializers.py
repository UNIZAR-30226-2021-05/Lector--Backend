from rest_framework import serializers

from .models import Usuario, Preferencias, Guardar, Libro
import sys
import os.path

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from libro.models import Libro
from libro.serializers import LibroSerializer


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

class GuardarSerializer(serializers.ModelSerializer):
    ISBN = serializers.SerializerMethodField('lee_libro')

    def lee_libro(self, Guardar):
        return Guardar.libro.ISBN
        
    class Meta:
        model = Guardar
        fields = [
            "ISBN",
            "leyendo",
            "currentOffset",
        ]
        
class ImageSerializer(serializers.Serializer):
    """
    API endpoint
    """
    url=serializers.CharField()


class ColeccionSerializer(serializers.Serializer):
    """
    API endpoint
    """
    titulo = serializers.CharField()
    listaLibros = LibroSerializer(many=True)  # A nested list of 'edit' items.


