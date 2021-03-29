from django.shortcuts import render
from .serializers import LibroSerializer
from .models import Libro

from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.

class libroView(APIView):

    def get(self, request, pk):
        '''
        Devuelve el libro solicitado
        '''
        libro = Libro.objects.get(ISBN=pk)
        #libro = get_object_or_404(Libro, ISBN=pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    def put(self, request, pk):
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
        queryset = libro.objects.all()
        serializer = LibroSerializer(queryset, many = True)
        return Response(serializer.data)