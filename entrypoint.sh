#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata main.json
python manage.py runserver 0.0.0.0:8000