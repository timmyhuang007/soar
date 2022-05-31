import logging
from traceback import format_exc
from typing import AsyncIterable, Optional
from asgiref.sync import sync_to_async
from soar import faust_app as app
from seap.models import Event
from seap.serializers import EventSerializer

logger = logging.getLogger(f'faulst.{__name__}')

@app.agent(app.topic('soar_events'), value_serializer='raw', concurrency=1)
async def event_serialize(stream:AsyncIterable) -> Optional[Event]:
    async for value in stream:
        try:
            event = EventSerializer(data=value)
            await sync_to_async(event.is_valid)(raise_exception=True)
            await sync_to_async(event.save)()
        except:
            logger.warning(format_exc())
            event = None
        yield event
