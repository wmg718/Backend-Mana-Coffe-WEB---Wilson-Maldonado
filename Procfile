release: python manage.py collectstatic --noinput
web: gunicorn Cafe_Web.wsgi:application --bind 0.0.0.0:$PORT

