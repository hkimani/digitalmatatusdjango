#!/bin/bash

cd /opt/digimatt/gtfs

export DJANGO_SETTINGS_MODULE=gtfs.settings

# TODO: // Wait for one minute for the sql server to start
# TODO: // IMPLEMENT

python manage.py migrate --noinput --run-syncdb

## collect statics
echo "Collecting the static files... I will not post the progress"
python manage.py collectstatic --noinput --verbosity 0
echo "Finished collecting the static files"


echo "Creating the default superuser ..."
python -m django_createsuperuser "admin" "${MYSQL_ROOT_PASSWORD}" "${USER_EMAIL}"
echo "Superuser created ..."

# Server start
echo "Starting server ..."
python manage.py runserver 0.0.0.0:8000