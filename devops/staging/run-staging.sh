#!/bin/sh

exec pip install -r /usr/src/app/requirements/staging.txt
exec gunicorn -w 4 vulgar.wsgi.application