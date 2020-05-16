#!/bin/sh

pip install -r /usr/src/app/requirements/staging.txt
python manage.py collectstatic --noinput
python manage.py migrate --fake-initial

# Create a user if doesn't exist
python manage.py shell << END
from django.contrib.auth.models import User
user = User.objects.create_user('vulgar', password='vulgar')
END

exec gunicorn -w 4 vulgar.wsgi -b 0.0.0.0:8000