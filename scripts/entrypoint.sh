#!/bin/bash

cd /opt/digimatt

export DJANGO_SETTINGS_MODULE=gtfs.settings

# TODO: // Wait for one minute for the sql server to start
# TODO: // IMPLEMENT

# TODO: // Make migrations and migrate

echo "Creating the default superuser ..."
python -m django_createsuperuser "admin" "${MYSQL_ROOT_PASSWORD}" "${USER_EMAIL}"
echo "Superuser created ..."

# Server start
echo "Starting server ..."
python manage.py runserver 0.0.0.0:8000