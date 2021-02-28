#!/bin/bash
#Cambiar a directorio raiz del proyecto
cd ..
pip freeze | grep -v "pkg-resources" > requirements.txt
git add .
echo "Añade un comentario al git commit: "
read comentario
#Actualizar commit en git
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

