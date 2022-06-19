import json
import logging
from datetime import datetime
from traceback import format_exc
from typing import AsyncIterable, Tuple

from asgiref.sync import sync_to_async
from benedict import benedict
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from faust import Stream

from seap.serializers import EventSerializer
from soar import faust_app as app
from soar.settings import MY_ELASTICSEARCH

logger = logging.getLogger(f'faulst.{__name__}')

class ElasticsearchSink:
    def __init__(self, topic:str):
        self.topic = topic
        self.es = AsyncElasticsearch(
            hosts = MY_ELASTICSEARCH['hosts'],
            verify_certs = False,
            ssl_show_warn = False,
            http_auth = (MY_ELASTICSEARCH['username'], MY_ELASTICSEARCH['password'])
        )
    
    def expand(self, record:dict) -> Tuple[str,str]:
        record['@timestamp'] = datetime.now().astimezone()
        index = json.dumps({
            'index': {
                '_index': f"{self._topic}-{record['@timestamp'].strftime('%Y.%m.%d')}"
            }
        })
        data = benedict(record).to_json()
        return index, data

    async def bulk(self, stream:Stream):
        async for records in stream.take(100, within=10):
            yield await async_bulk(
                client = self.es,
                actions = records,
                expand_action_callback = self.expand,
                stats_only = True,
                max_retries = 3
            )

async def event_serialize(stream:AsyncIterable) -> dict:
    async for value in stream:
        try:
            serializer = EventSerializer(data=value)
            await sync_to_async(serializer.is_valid)(raise_exception=True)
            event = (await sync_to_async(serializer.save)()).__dict__
            event.pop('_state')
        except:
            msg = format_exc()
            logger.warning(msg)
            event = {'message': msg}
        yield event
