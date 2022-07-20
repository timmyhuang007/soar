import faust
from elasticsearch_dsl.utils import AttrDict
from .settings import PROJECT_NAME, MY_FAUST

app = faust.App(PROJECT_NAME)
app.config_from_object(AttrDict(MY_FAUST))