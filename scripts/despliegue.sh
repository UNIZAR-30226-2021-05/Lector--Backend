#!/bin/bash
######################################################################
# @author      : grupo 5
# @file        : despliegue.sh
# @created     : domingo feb 28, 2021 19:19:01 CET
#
# @description : Despliegue de repositorio git en heroku
######################################################################
#Cambiar a directorio raiz del proyecto
cd ..
#Actualizar librerías necesarias para heroku
pip freeze | grep -v "pkg-resources" > requirements.txt
#Actualizar repositorio git
git add .
#echo "Añade un comentario al git commit: "
read comentario
git commit -m "$comentario"
#Actualizar commit en heroku
heroku maintenance:on
git push heroku
heroku maintenance:off
#Visualizar aplicación desplegada
heroku open

#ver log del servidor en producción
#heroku logs --tail --app rocky-waters-55301
#Probar despliegue en local
#heroku local
#Dejar de dar servicio
#heroku ps:scale web=0

