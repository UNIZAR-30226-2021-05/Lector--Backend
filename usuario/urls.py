from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
   #path('usuario/', views.usuarioListView.as_view()),
   path('<str:pk>', views.usuarioView.as_view()),
   path('preferencias/<str:pk>', views.preferenciasView.as_view()),
   path('guardar/<str:usrk>', views.guardarView.as_view()),
   path('guardar/<str:usrk>/<str:libk>', views.guardarLibroView.as_view())

]