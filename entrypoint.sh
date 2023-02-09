#!/bin/sh
wait-for-db
python manage.py migrate
exec "$@"
