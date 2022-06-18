import os
from celery import Celery
from .settings import MY_CELERY

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soar.settings')

conf = dict(MY_CELERY)
app = Celery('soar', broker=conf.pop('broker_url'))

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(conf)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()