from django.shortcuts import render
from .serializers import*
from utils.dropbox.operations import* 
from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

# Create your views here.
class textFieldView():

    def __init__ (self, text, finalOffset, realCharacters):
        self.text=text
        self.finalOffset=finalOffset
        self.realCharacters=realCharacters

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


class DownloadView(APIView):

    def get(self,request,file):
        '''
        Descarga en back el libro solicitado
        '''
        libro = Libro.objects.get(ISBN=file)
        serializer = LibroSerializer(libro)
        s = serializer.data["titulo"] + "." + serializer.data["formato"]
        aux = download_file(s)
        if (aux):
            return Response("Se ha descargado", status=200)
        else:
            return Response("Error en descarga", status=500)

class TextView(APIView):

    def get(self, request,file,ini_offset,characters):   
        '''
        Devuelve el numero de caracteras a partir del offset del libro solicitado
        '''
        libro = Libro.objects.get(ISBN=file)
        serializer = LibroSerializer(libro)
        s = serializer.data["titulo"] + "." + serializer.data["formato"]
        name_local=translate_file(s)
        f=open(name_local, 'r')
        f.seek(ini_offset,0)
        text=f.read(characters)
        if (len(text)==characters):
            send_text=text.rsplit(" ",1)
            send_characters=characters-len(send_text[1])
            textField= textFieldView(text=send_text[0],finalOffset=ini_offset+send_characters,realCharacters=send_characters)
        else:
            textField= textFieldView(text=text,finalOffset=ini_offset+characters,realCharacters=characters)
        
        serializer = TextSerializer(textField)
        return Response(serializer.data)
    

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