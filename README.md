## Setup Projcet

    git clone https://github.com/AKOWAKOU/django.git

    cd django

## Create .venv env and Active Env


    python3.9 -m venv .venv

    source .venv/bin/active

## Run Migrations 

    cd todo/

    python manage.py makemigrations

    python manage.py migrate    

## Run Server

    python manage.py runserver

     http://127.0.0.1:8000//api/schema/swagger-ui/
