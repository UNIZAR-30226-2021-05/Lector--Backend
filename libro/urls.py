from django.urls import include, path, re_path
from rest_framework import routers
from . import views

from django.conf.urls import url

urlpatterns = [
   path('offset/<str:file>/<int:ini_offset>/<int:characters>', views.TextView.as_view()),
   path('download/<str:file>',views.DownloadView.as_view()),
   path('<str:pk>', views.libroView.as_view()),
   path('todos/', views.libroListView.as_view()),
   path('autor/<str:pk>', views.autorView.as_view()),
   path('genero/<str:pk>', views.generoView.as_view()),
]