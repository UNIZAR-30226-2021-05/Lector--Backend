from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usuario',views.UsuarioViewSet)

urlpatterns = [
   # url(r'^$', views.index, name='index'),
   path('', include(router.urls)),
   url(r'^rest-auth/', include('rest_auth.urls')),
   url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]