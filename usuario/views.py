import re

from rest_framework import serializers
from libro.models import Libro
import usuario
from .serializers import UsuarioSerializer, PreferenciasSerializer, GuardarSerializer, ImageSerializer
from .models import Usuario, Preferencias, Guardar
from utils.dropbox.operations import* 


from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from utils.dropbox.operations import* 


#GET /usuario/<id> -> SELECT  nombre, apellidos, correo
#PUT /usuario/<id> -> UPDATE usuario

#GET /configuracion/<id_usuario> -> SELECT * from configuracion
#PUT /configuracion/<id_usuario> -> UPDATE configuracion
class imageFieldView():

    def __init__ (self, url):
        self.url=url

class userFieldView():

    def __init__ (self, id, username, email, pathFoto):
        self.id=id
        self.username=username
        self.email=email
        self.pathFoto=pathFoto

class usuarioView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        '''
        Devuelve el perfil del usuario
        '''
        user= Usuario.objects.get(username=pk)
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        '''
        Modifica el perfil del usuario
        '''
        usuario = Usuario.objects.get(username=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        s = ""
        if request.data["pathFoto"]:
            s = get_url(request.data["pathFoto"])
        
        if serializer.is_valid():
            userField =userFieldView(id=serializer.data["id"],username=request.data["username"],email=request.data["email"],pathFoto=s)
            serializer2 = UsuarioSerializer(userField)
            usuario.pathFoto = s
            usuario.email = request.data["email"]
            usuario.save()
            return Response(serializer2.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class preferenciasView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        '''
        Devuelve las preferencias del usuario
        '''
        pref= Preferencias.objects.get(usuario__username=pk)
        serializer = PreferenciasSerializer(pref)
        return Response(serializer.data)

    def put(self, request, pk):
        '''
        Modifica las preferencias del usuario
        '''
        pref = Preferencias.objects.get(usuario__username=pk)
        serializer = PreferenciasSerializer(pref, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class guardarLibroView(APIView):

    def post(self, request, usrk, libk):
        user = Usuario.objects.get(username=usrk)
        serializerU = UsuarioSerializer(user)
        usrk = serializerU.data['id']
        try:
            guard = Guardar.objects.get(usuario=usrk, libro=libk)#¿Puede fallar? Sacar un libro en concreto. Si existe modifica, si no crea
            #serializer = GuardarSerializer(guard, data=request.data)
            serializer = GuardarSerializer(guard, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            #No existe el libro en guardados, lo creamos.
            libro = Libro.objects.get(ISBN=libk)
            guard = Guardar(usuario=user, libro=libro, puntuacion=0, currentOffset=request.data["currentOffset"], leyendo=True)
            guard.save()
            serializer = GuardarSerializer(guard)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class guardarView(APIView):

    def get(self, request, usrk):
        '''
        Devuelve las preferencias del usuario
        '''
        user = Usuario.objects.get(username=usrk)
        serializerU = UsuarioSerializer(user)
        usrk = serializerU.data['id']
        guard = Guardar.objects.filter(usuario=usrk)
        serializer = GuardarSerializer(guard, many=True)
        return Response(serializer.data)

class imageView (APIView):
    def get (self,request,pk):
        '''
        Devuelve la url correspondiente a  la imagen de icono del usr
        '''
        aux=get_url(pk)
        print(aux)
        imageField= imageFieldView(url=aux)
        serializer = ImageSerializer(imageField)
        return Response(serializer.data)



# get /usuario/coleccion/<username:str> titulo = "accion"
# put /usuario/coleccion/rename/<username:str>/ oldTitulo = "accion" newTitulo = "drama" 
# put /usuario/coleccion/add/<username:str>/ libro = libro



'''
#LISTA USUARIO
class usuarioListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset= Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many = True)
        return Response(serializer.data)
'''

