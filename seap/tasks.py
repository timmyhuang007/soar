from celery import shared_task
from celery.utils.log import get_task_logger
from celery_once import QueueOnce

logger = get_task_logger(__name__)

@shared_task(base=QueueOnce, once={'graceful':True})
def add(x,y):
    return x+y
