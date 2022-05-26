import json
from typing import AsyncIterable
from soar import faust_app as app
from seap.models import Event
from seap.serializers import EventSerializer

@app.agent(app.topic('soar_events'), value_serializer='raw', concurrency=1)
async def event_serialize(stream:AsyncIterable) -> Event:
    async for value in stream:
        event = EventSerializer(data=json.loads(value))
        event.save()
        yield event
