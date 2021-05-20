#!/bin/bash
######################################################################
# @author      : grupo 5
# @file        : psql_configuracion
# @created     : domingo feb 28, 2021 19:19:01 CET
#
# @description : Configuración inicial postgresql y migración de django
#                SOLO EJECUTAR LA PRIMERA VEZ
######################################################################

which psql
if [ "$?" -gt "0" ];then
    echo "ERROR: postgreSQL no está instalado"
elif [ $USER != "postgres" ];then
    echo "ERROR: logeate como postgres: sudo su - postgres"
else
    psql << EOF
CREATE DATABASE lectoruser;
CREATE USER lectoruser WITH PASSWORD 'lectoruser';
ALTER ROLE lectoruser SET client_encoding TO 'utf8';
ALTER ROLE lectoruser SET default_transaction_isolation TO 'read committed';
ALTER ROLE lectoruser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE lectoruser TO lectoruser;
EOF

fi
