from django.shortcuts import render
from .serializers import*
from .models import Libro
from utils.dropbox.operations import* 

from rest_framework.views import APIView
from rest_framework.response import Response 

from rest_framework import generics

# Create your views here.
class textFieldView():

    def __init__ (self, text, finalOffset, realCharacters):
        self.text=text
        self.finalOffset=finalOffset
        self.realCharacters=realCharacters

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

class TextView(APIView):

    def get(self, request,file,ini_offset,characters):   
        '''
        Devuelve el numero de caracteras a partir del offset del libro solicitado
        '''
        name_local=read_file(file)
        f=open(name_local, 'r')
        f.seek(ini_offset,0)
        text=f.read(characters)
        textField= textFieldView(text=text,finalOffset=ini_offset+characters,realCharacters=characters)
        serializer = TextSerializer(textField)
        return Response(serializer.data)
    

#LISTA LIBRO
class libroListView(APIView):

    def get(self, request):
        queryset = libro.objects.all()
        serializer = LibroSerializer(queryset, many = True)
        return Response(serializer.data)