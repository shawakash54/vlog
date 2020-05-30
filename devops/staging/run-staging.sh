#!/bin/sh

pip install -r /usr/src/app/requirements/staging.txt
python manage.py collectstatic --noinput
python manage.py migrate --fake-initial

# Create a user if doesn't exist
python manage.py shell << END
from django.contrib.auth.models import User
user = User.objects.create_user('trikonindia', password='trikonindia')
END

# Number of workers should be 2-4 per core in the server(2*CPU)+1
# We can also set --threads=2
# gunicorn --worker-class=gevent --worker-connections=1000 --workers=3
exec gunicorn --worker-class=gevent --worker-connections=1000 --workers=3 vulgar.wsgi -b 0.0.0.0:8000