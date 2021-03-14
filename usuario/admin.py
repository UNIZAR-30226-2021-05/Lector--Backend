from django.contrib import admin

# Register your models here.
from .models import Usuario, Configuracion
admin.site.register(Usuario)
admin.site.register(Configuracion)