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
        port = libro.portada
        sino = libro.sinopsis
        auto = libro.autor
        if 'portada' in request.data and request.data["portada"]:
            port = get_url(request.data["portada"])
        if 'sinopsis' in request.data and request.data["sinopsis"]:
            sino = request.data["sinopsis"]
        if 'autor' in request.data and request.data["autor"]:
            auto = request.data["autor"]
        lib = Libro(ISBN=request.data["ISBN"], pathLibro=request.data["pathLibro"], titulo=request.data["titulo"], portada=port, 
            sinopsis=sino, formato=request.data["formato"], autor=auto)
        lib.save()
        serializer = LibroSerializer(lib)
        return Response(serializer.data)


class DownloadView(APIView):

    def get(self,request,file):
        '''
        Descarga en back el libro solicitado
        '''
        aux = download_file(file)
        if (aux):
            return Response("Se ha descargado", status=200)
        else:
            return Response("Error en descarga", status=500)

class TextView(APIView):

    def get(self, request,file,ini_offset,characters):   
        '''
        Devuelve el numero de caracteras a partir del offset del libro solicitado
        ''' 
        name_local=translate_file(file)
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