#!/bin/sh
wait-for-db
python manage.py migrate
python manage.py collectstatic --noinput
exec "$@"
