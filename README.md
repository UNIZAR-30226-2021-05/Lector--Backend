#Software requerido pip3  
python-3.6.9  
Django-3.1.7  

# Instalar librerías necesarias:
python -r "requirements.txt"  

/////////////////DESARROLLO//////////////////

#Configuración entorno virtual con python3.6
##Instalación
sudo pip3 install virtualenvwrapper
##Añadir paths necesarios en ~/.bashrc
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export PROJECT_HOME=$HOME/Escritorio
source /usr/local/bin/virtualenvwrapper.sh
##Actualizar cambios
source ~/.bashrc
##Crear entorno virtual llamado 'lector'
mkvirtualenv --python=python3.6 lector
#Comandos útiles
comandos:
    deactivate              //Salir de entorno actual
    workon                  //Listar entornos disponibles
    workon <lector>         //Activar entorno
    rmvirtualenv <entorno>  //Borrar entorno
#Actualizar requirements.txt
pip3 freeze > requirements.txt


