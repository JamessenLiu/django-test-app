import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

app = Celery(
    'celery',
    broker="amqp://root:root@localhost:32780/broker"
)

app.config_from_object(
    "apps.tasks.celery_config", silent=True)
