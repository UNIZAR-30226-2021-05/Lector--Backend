from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UsuarioSerializer
from .models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]





'''
def index(request):
    b = Usuario(nickname='test',password=make_password('a', None, 'md5'),correo='a',nombre='a',apellidos='a',esAdmin=False)
    b.save()
    
    num_users=Usuario.objects.all().count()
    num_admins=Usuario.objects.filter(esAdmin__exact='True').count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'user.html',
        context={'num_users':num_users, 'num_admins':num_admins},
    )
'''