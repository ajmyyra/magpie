#!/bin/bash

python3 manage.py migrate

DJANGO_SETTINGS="prod.settings"
if [[ -z "${DEPLOY_ENV}" ]]; then
  DJANGO_SETTINGS=${DEPLOY_ENV}
fi

echo "Running uwsgi with settings file: ${DJANGO_SETTINGS}"

uwsgi --strict \
    --chdir=/usr/src/app \
    --plugin python3 --plugin http \
    --env DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS} \
    --master \
    --workers 8 \
    --thunder-lock \
    --http :9876 \
    --need-app \
    --disable-logging \
    --log-4xx --log-5xx \
    --wsgi magpie.wsgi:application
