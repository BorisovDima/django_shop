#!/bin/bash


touch error_docker.log
touch logs_docker.log

touch django_shop/error.log
touch django_shop/logs.log

docker-compose up --build

