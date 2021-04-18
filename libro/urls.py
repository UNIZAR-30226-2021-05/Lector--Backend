from django.urls import include, path, re_path
from rest_framework import routers
from . import views

from django.conf.urls import url

urlpatterns = [
   path('offset/<str:file>/<int:ini_offset>/<int:characters>', views.TextView.as_view()),
   path('<str:pk>', views.libroView.as_view()),
]