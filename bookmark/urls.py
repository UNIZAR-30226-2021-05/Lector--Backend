from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
   path('<str:usrk>/<str:libk>', views.bookmarkView.as_view()),
   path('<str:idk>', views.bookmarkView.as_view()),
   #path('todos/', views.bookmarkListView.as_view()),
]