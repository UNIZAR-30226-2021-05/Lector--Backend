import re

from rest_framework import serializers
from libro.models import Libro
import usuario
from .serializers import *
from .models import *
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
    
class coleccionFieldView():

    def __init__ (self, titulo, listaLibros):
        self.titulo=titulo
        self.listaLibros=listaLibros

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
        s = usuario.pathFoto
        if 'pathFoto' in request.data and request.data["pathFoto"]:
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

class guardarLeerLibroView(APIView):

    def get(self, request, usrk, libk):
            user = Usuario.objects.get(username=usrk)
            serializerU = UsuarioSerializer(user)
            usrk = serializerU.data['id']
            try:
                guard = Guardar.objects.get(usuario=usrk, libro=libk)
                serializer = GuardarSerializer(guard)
                return  Response(serializer.data)
            except:
                return Response({'error': 'El usuario no tiene el libro'})


class guardarLibroView(APIView):

    def get(self, request, usrk, libk):
        user = Usuario.objects.get(username=usrk)
        serializerU = UsuarioSerializer(user)
        usrk = serializerU.data['id']
        try:
            guard = Guardar.objects.get(usuario=usrk, libro=libk)
            
            return Response({'correcto': 'El usuario tiene el libro'})
        except:
            return Response({'error': 'El usuario no tiene el libro'})

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
            guard = Guardar(usuario=user, libro=libro, puntuacion=0, currentOffset=request.data["currentOffset"], leyendo=False)
            guard.save()
            serializer = GuardarSerializer(guard)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrarLibroView(APIView):

    def post(self, request, usrk, libk):
        user = Usuario.objects.get(username=usrk)
        serializerU = UsuarioSerializer(user)
        usrk = serializerU.data['id']

        if Guardar.objects.filter(usuario = usrk, libro = libk).exists():
            #Caso coleccion existe
            Guardar.objects.filter(usuario = usrk, libro = libk).delete()
            return Response({'Correcto':'Libro eliminado de la lista'})
        else:
            return Response({'error': 'El usuario no tiene guardado el libro'})
        
class guardarView(APIView):

    def get(self, request, usrk):
        '''
        Devuelve los libros del usuario
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

#DEVOLVER COLECCION
# Si titulo == null -> ERROR
# get /usuario/coleccion/<username:str> titulo = "accion" 

#AÑADIR/ACTUALIZAR COLECCION. 
#   Si título == null -> ERROR
#   sino si libros = [] -> si existe coleccion, actualiza titulo, si no la crea
#   Sino si libros != [] -> Si existe coleccion, actualiza titulo y añade libros, si no la crea.
# put /usuario/coleccion/<username:str>/ titulo = "accion" libros = {libro} 

#ELIMINAR COLECCION
#   Si título == null -> ERROR
# put /usuario/coleccion/del/<username:str>/ titulo = "accion"                                                       


class coleccionView (APIView):
    def get (self,request,username,titulo):
        '''
        Devuelve una coleccion del usuario si existe
        '''
        if Coleccion.objects.filter(usuario__username=username, titulo = titulo).exists():
            #Caso existe la coleccion
            col = Coleccion.objects.filter(usuario__username=username, titulo = titulo).first()
            agru = Agrupar.objects.filter(coleccion__id = col.id)
            libros = []
            for l in agru:
                libros += [{
                    "ISBN":l.libro.ISBN, 
                    "formato":l.libro.formato,
                    "autor": l.libro.autor.nombre,
                    "pathLibro": l.libro.pathLibro,
                    "portada": l.libro.portada,
                    "sinopsis": l.libro.sinopsis,
                    "titulo": l.libro.titulo
                    }]
            return Response({'titulo': col.titulo, 'libros': libros})
        else:
            return Response({'error': 'No existe coleccion'})

    def put (self, request, username, titulo):
        '''
        Añade una coleccion al usuario si no existe
        '''
        idUsuario = Usuario.objects.get(username = username)
        if Coleccion.objects.filter(usuario = idUsuario, titulo = titulo).exists():
            #Caso existe la coleccion
            #if request.data["titulo"] != "" and request.data["libros"] == "":
            #    col = Coleccion.objects.filter(usuario = idUsuario, titulo = request.data["titulo"])
            #    col.titulo = titulo 
            #    col.save()
            #    return Response({'Correcto':'Coleccion renombrada'})
            return Response({'error': 'Ya existe coleccion'})
        else:
            #Caso no existe la coleccion
            col = Coleccion(usuario = idUsuario, titulo = titulo)
            col.save()
            libros = request.data["libros"].split(",")
            for isbn in libros:
                if not Agrupar.objects.filter(libro = isbn, coleccion = col.id).exists():
                    #Caso la tupla libro,coleccion en agrupar no existe
                    print("tupla no existe " + isbn)
                    if Libro.objects.filter(ISBN=isbn).exists():
                        #Caso el libro a aádir a la coleccion existe
                        l = Libro.objects.filter(ISBN=isbn).first()
                        agru = Agrupar(libro = l, coleccion = col)
                        print("Voy a guardar")
                        agru.save()
            return Response({'correcto' : 'Coleccion añadida'})

class coleccionRenameView (APIView):
    def put (self,request,username):
        idUsuario = Usuario.objects.get(username = username)
        idU = idUsuario.id
        if Coleccion.objects.filter(usuario = idU, titulo = request.data["oldTitulo"]).exists():
            #Caso existe la coleccion
            if request.data["newTitulo"] != "" :
                #Caso nuevo título no es vacio
                col = Coleccion.objects.filter(usuario = idU, titulo = request.data["oldTitulo"]).first()
                col.titulo = request.data["newTitulo"] 
                col.save()
                return Response({'Correcto':'Coleccion renombrada'})
            return Response({'error': 'Nuevo titulo vacio'})
        else:
            return Response({'error': 'No existe coleccion'})

class coleccionDeleteView (APIView):
    def put (self,request,username):
        idUsuario = Usuario.objects.get(username = username)
        if Coleccion.objects.filter(usuario = idUsuario, titulo = request.data["titulo"]).exists():
            #Caso coleccion existe
            Coleccion.objects.filter(usuario = idUsuario, titulo = request.data["titulo"]).delete()
            return Response({'Correcto':'Coleccion eliminada'})
        else:
            return Response({'error': 'No existe coleccion'})

class colecctionesListView(APIView):

    def get(self, request, username):
        idUsuario = Usuario.objects.get(username = username)
        queryset = Coleccion.objects.filter(usuario = idUsuario)
        serializer = ColeccionesListSerializer(queryset, many = True)
        return Response(serializer.data)


'''
#LISTA USUARIO
class usuarioListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset= Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many = True)
        return Response(serializer.data)
'''

