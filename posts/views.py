from django.shortcuts import render
from utils.dropbox.operations import* 
from libro.models import *
from posts.models import Post

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
# Create your views here.

class rateView(APIView):
    #permission_classes = (IsAuthenticated,)

    def put(self,request,libk,punt):
        '''
        Publica un tweet con la valoracion de un libro
        '''
        libro = Libro.objects.get(ISBN=libk)
        if (punt >= 0 and punt <=5):
            #Post.objects.create(title='My First Post', content='El libro '+libro.data['titulo'] +' ha sido valorado con un '+punt)
            Post.objects.create(title='El libro '+libro.titulo +' ha sido valorado con un '+str(punt))
            #print('El libro '+libro.titulo +' ha sido valorado con un '+str(punt))
            return Response("Libro valorado", status=200)
        else:
            return Response("Error en valoracion, puntuacion incorrecta", status=500)