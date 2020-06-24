### Commands
- python manage.py runserver [To start server]
- python manage.py collectstatic --noinput [collect static content in static folder]
- python manage.py makemessages -l hi [generate .po file for this language]
- python manage.py compilemessages --use-fuzzy [compile language from .po file to be used in the app]
- python manage.py createcachetable [used to create a cache table in the database]
- python manage.py cities_light [used for populating database with cities]
- psql -U vulgar -d vulgar < ./vulgar_initial.db [To copy contents from pg_dump]
- python manage.py createsuperuser [creating superusers]
- sudo docker-compose -f docker-compose.yml -f devops/production/docker-compose.yml up -d --build vulgar
- sudo docker-compose -f docker-compose.yml -f devops/production/docker-compose.yml exec vulgar bash -c "python manage.py migrate"
- sudo docker-compose -f docker-compose.yml -f devops/production/docker-compose.yml exec vulgar bash -c "python manage.py collectstatic --noinput"

