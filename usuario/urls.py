from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
   #path('usuario/', views.usuarioListView.as_view()),
   path('<str:pk>', views.usuarioView.as_view()),

]