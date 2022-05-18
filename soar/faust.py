import os
import faust
from attrdict import AttrDict
from .settings import PROJECT_NAME, MY_FAUST

# set the default Django settings module for the 'faust' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soar.settings')

app = faust.App(PROJECT_NAME, autodiscover=True)
app.config_from_object('django.conf:settings', namespace='FAUST')
app.config_from_object(AttrDict(MY_FAUST))