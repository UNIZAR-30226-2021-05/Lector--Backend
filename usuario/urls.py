from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
   #path('usuario/', views.usuarioListView.as_view()),
   path('<str:pk>', views.usuarioView.as_view()),
   path('preferencias/<str:pk>', views.preferenciasView.as_view()),
   path('guardar/<str:usrk>', views.guardarView.as_view()),
   path('guardar/<str:usrk>/<str:libk>', views.guardarLibroView.as_view()),
   path('image/<str:pk>', views.imageView.as_view()),
   path('coleccion/rename/<str:username>', views.coleccionRenameView.as_view()),
   path('coleccion/delete/<str:username>', views.coleccionDeleteView.as_view()),
   path('coleccion/<str:username>/<str:titulo>', views.coleccionView.as_view()),
   path('coleccion/<str:username>', views.colecctionesListView.as_view()),
]