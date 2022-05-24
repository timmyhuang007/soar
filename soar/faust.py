import faust
from attrdict import AttrDict
from .settings import PROJECT_NAME, MY_FAUST, MY_APPS

app = faust.App(PROJECT_NAME)
app.config_from_object(AttrDict(MY_FAUST))
app.discover(*MY_APPS, ignore=['rest_framework'])