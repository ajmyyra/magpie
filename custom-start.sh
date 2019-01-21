#!/bin/bash

if [[ ! -z "${ONLY_MIGRATE}" ]]; then
  python3 manage.py migrate
  exit 0
fi

uwsgi --strict \
    --chdir=/usr/src/app \
    --plugin python3 --plugin http \
    --master \
    --workers 8 \
    --thunder-lock \
    --http :9876 \
    --need-app \
    --disable-logging \
    --log-4xx --log-5xx \
    --wsgi magpie.wsgi:application
