from django.contrib import admin

# Register your models here.
from .models import Usuario, Preferencias
admin.site.register(Usuario)
admin.site.register(Preferencias)