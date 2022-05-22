import faust
from attrdict import AttrDict
from .settings import PROJECT_NAME, MY_FAUST, MY_APPS

app = faust.App(PROJECT_NAME, autodiscover=MY_APPS)
app.config_from_object(AttrDict(MY_FAUST))