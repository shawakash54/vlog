#!/bin/sh

pip install -r /usr/src/app/requirements/dev.txt
exec python /usr/src/app/manage.py runserver_plus 0.0.0.0:8000