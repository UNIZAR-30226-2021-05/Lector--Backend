from django.shortcuts import render
from .serializers import BookmarkSerializer
from .models import Bookmark

from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.
class bookmarkView(APIView):

    def get(self, request, usrk, libk):
        '''
        Devuelve el bookmark solicitado
        '''
        bookmark = bookmark.objects.get(Usuario = usrk, Libro = libk)
        #bookmark = get_object_or_404(bookmark, Usuario = usrk, Libro = libk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    def put(self, request, usrk, libk):
        '''
        Modifica un bookmark
        '''
        bookmark = Bookmark.objects.get(Usuario = usrk, Libro = libk)
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)