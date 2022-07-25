import os
import django
from celery import Celery
from django.conf import settings

config = os.getenv("MODE")
if config is None:
    config = "django_app.local"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", config)
django.setup()


RABBIT_MQ_USER = settings.RABBIT_MQ_USER
RABBIT_MQ_PASSWORD = settings.RABBIT_MQ_PASSWORD
RABBIT_MQ_IP = settings.RABBIT_MQ_IP
RABBIT_MQ_PORT = settings.RABBIT_MQ_PORT

app = Celery(
    'celery',
    broker="amqp://{0}:{1}@{2}:{3}/broker".format(
        RABBIT_MQ_USER, RABBIT_MQ_PASSWORD, RABBIT_MQ_IP, RABBIT_MQ_PORT
    )
)

app.config_from_object(
    "apps.tasks.celery_config", silent=True)
