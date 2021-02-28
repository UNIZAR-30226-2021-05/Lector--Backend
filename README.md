## Software requerido  
pip3  
python3    
Django-3.1.7    


## Configuración entorno virual python

```bash 
#Instalación virtualenvwrapper
sudo pip3 install virtualenvwrapper
#Añadir paths necesarios en ~/.bashrc
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export PROJECT_HOME=$HOME/Escritorio
source /usr/local/bin/virtualenvwrapper.sh
#Actualizar cambios
source ~/.bashrc
#Crear entorno virtual de python3 llamado 'lector'
mkvirtualenv --python=python3 lector
#Comandos útiles entorno virtual
comandos:
    deactivate              //Salir de entorno actual
    workon                  //Listar entornos disponibles
    workon <lector>         //Activar entorno
    rmvirtualenv <entorno>  //Borrar entorno
```
## Despliegue en heroku
```bash
#Crear cuenta en heroku.com
#Autenticación desde consola
heroku login
#Creación de aplicación en heroku
heroku create lector
#Ligar repositorio a nuestra app en heroku
heroku git:remote -a lector
#Ejecutar script de despliegue
bash despliegue.sh
```

