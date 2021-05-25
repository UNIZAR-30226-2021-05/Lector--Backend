from django.urls import include, path, re_path
from rest_framework import routers
from . import views

from django.conf.urls import url

urlpatterns = [
   path('<str:libk>/<int:punt>', views.rateView.as_view()),
]