from usuario import views
from django.shortcuts import render

import usuario
from .serializers import BookmarkSerializer
from usuario.serializers import UsuarioSerializer
from .models import Bookmark, Usuario, Libro

from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.
class bookmarkView(APIView):

    def get(self, request, usrk, libk):
        '''
        Devuelve el bookmark solicitado
        '''
        
        user = Usuario.objects.get(username=usrk)
        serializerU = UsuarioSerializer(user)
        usrk = serializerU.data['id']
        bookmarkSet = Bookmark.objects.filter(Usuario = usrk, Libro = libk)
        #bookmark = get_object_or_404(bookmark, Usuario = usrk, Libro = libk)
        serializer = BookmarkSerializer(bookmarkSet, many = True)
        return Response(serializer.data)
        
    '''
    def get(self, request, idk):
        bookmark = Bookmark.objects.get(id = idk)
        #bookmark = get_object_or_404(bookmark, Usuario = usrk, Libro = libk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)
    '''

    def post(self, request, idk):
        '''
        Modifica un bookmark
        '''
        bookmark = Bookmark.objects.get(id = idk)
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class crearBookmarkView(APIView):
    def post(self, request, usrk, libk):
        user = Usuario.objects.get(username=usrk)
        lib = Libro.objects.get(ISBN=libk)
        bookm = Bookmark(Usuario=user, Libro=lib, esAnotacion=True, cuerpo=request.data["cuerpo"], offset=request.data["offset"])
        bookm.save()
        serializer = BookmarkSerializer(bookm)
        return Response(serializer.data)
        
class bookmarkListView(APIView):

    def get(self, request):
        queryset = Bookmark.objects.all()
        serializer = BookmarkSerializer(queryset, many = True)
        return Response(serializer.data)