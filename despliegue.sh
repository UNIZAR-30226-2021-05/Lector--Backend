#!/bin/bash
pip freeze > requirements.txt
git add .
echo "Añade un comentario al git commit: "
read comentario
#Actualizamos commit en git
git commit -m "$comentario"
#Actualizamos commit en heroku
heroku maintenance:on
git push heroku
heroku maintenance:off
