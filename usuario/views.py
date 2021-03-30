from .serializers import UsuarioSerializer, PreferenciasSerializer
from .models import Usuario, Preferencias

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated



#GET /usuario/<id> -> SELECT  nombre, apellidos, correo
#PUT /usuario/<id> -> UPDATE usuario

#GET /configuracion/<id_usuario> -> SELECT * from configuracion
#PUT /configuracion/<id_usuario> -> UPDATE configuracion


class usuarioView(APIView):
    permission_classes = (IsAuthenticated,)

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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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



'''
#LISTA USUARIO
class usuarioListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset= Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many = True)
        return Response(serializer.data)
'''

