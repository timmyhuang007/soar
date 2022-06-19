# 必须首先初始化Django
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soar.settings')
django.setup()

from seap.agents import ElasticsearchSink, event_serialize

from .faust import app
from .settings import MY_APPS

if __name__ == '__main__':
    topic = 'soar_events'
    es_sink = app.agent(app.channel())(ElasticsearchSink(topic).bulk)
    event_agent = app.agent(
        app.topic(topic), value_serializer='raw', concurrency=1, sink=[es_sink]
    )(event_serialize)
    app.discover(*MY_APPS, ignore=['rest_framework'])
    app.main()
