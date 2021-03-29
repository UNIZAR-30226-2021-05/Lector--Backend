from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
   path('<str:pk>', views.libroView.as_view()),

]