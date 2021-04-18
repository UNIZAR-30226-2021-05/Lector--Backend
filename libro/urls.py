from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
   path('<str:pk>', views.libroView.as_view()),
   path('todos/', views.libroListView.as_view()),
   path('autor/<str:pk>', views.autorView.as_view()),
   path('genero/<str:pk>', views.generoView.as_view()),
]