from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class libroView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        '''
        Devuelve el libro solicitado
        '''
        libro = Libro.objects.get(ISBN=pk)
        #libro = get_object_or_404(Libro, ISBN=pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    def post(self, request, pk):
        '''
        Modifica un libro
        '''
        libro = Libro.objects.get(ISBN=pk)
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#LISTA LIBRO
class libroListView(APIView):

    def get(self, request):
        queryset = Libro.objects.all()
        serializer = LibroSerializer(queryset, many = True)
        return Response(serializer.data)

class autorView(APIView):
    def get(self, request, pk):
        '''
        Devuelve el autor
        '''
        autor = Autor.objects.get(nombre=pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

class generoView(APIView):
    def get(self, request, pk):
        '''
        Devuelve el genero
        '''
        gene = Genero.objects.get(genero=pk)
        serializer = GeneroSerializer(gene)
        return Response(serializer.data)