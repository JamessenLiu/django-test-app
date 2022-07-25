FROM python:3.6-slim-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD python3 manage.py migrate --settings django_app.dev \
    && uwsgi -w config.wsgi --http :8000 -p4 --env DJANGO_SETTINGS_MODULE=django_app.dev -d start \
    && daphne -b 0.0.0.0 -p 8001 --proxy-headers config.asgi:application > logs/asgi.log 2>&1 & \
    sh ./scripts/start_celery.sh \
