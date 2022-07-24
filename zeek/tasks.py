import asyncio
from datetime import datetime
from typing import List, Union

from aiodns import DNSResolver
from aiodns.error import ARES_ENOTFOUND, DNSError
from aioping import ping
from celery import shared_task
from celery.utils.log import get_task_logger
from celery_once import QueueOnce
from pycares import ares_query_a_result

from zeek.models import IntelAddr, Intelligence, IntelDomain

logger = get_task_logger(__name__)

@shared_task(base=QueueOnce, once={'graceful':True})
def check_domain_status_wrapper():
    intells = IntelDomain.objects.exclude(status=Intelligence.INDICATOR_STATUS.DELETED)
    results = asyncio.run(check_domain_status([i.domain for i in intells]))
    for result,intell in zip(results, intells):
        if isinstance(result, list):
            intell.ips = result
            if result:
                intell.status = Intelligence.INDICATOR_STATUS.ACTIVE.value
            else:
                intell.status = Intelligence.INDICATOR_STATUS.INACTIVE.value
            intell.save()

async def check_domain_status(domains:List[str]) -> List[Union[list,Exception]]:
    dns = DNSResolver()
    results = await asyncio.gather(*[dns.query(domain,'A') for domain in domains], return_exceptions=True)
    for i in range(len(results)):
        if isinstance(results[i], Exception):
            if isinstance(results[i],DNSError) and results[i].args[0]==ARES_ENOTFOUND:
                results[i] = []
        elif isinstance(results[i],list):
            results[i] = [r.host for r in results[i] if isinstance(r,ares_query_a_result)]
    return results

@shared_task(base=QueueOnce, once={'graceful':True})
def check_addr_status_wrapper():
    intells = IntelAddr.objects.exclude(status=Intelligence.INDICATOR_STATUS.DELETED)
    results = asyncio.run(check_addr_status([i.addr for i in intells]))
    for result,intell in zip(results, intells):
        if isinstance(result, (int,float)):
            intell.status = result
            intell.save()

async def check_addr_status(addrs:List[str]) -> List[Union[int,Exception]]:
    results = await asyncio.gather(*[ping(addr,10)*3 for addr in addrs], return_exceptions=True)
    for i in range(len(results)):
        if isinstance(results[i], Exception):
            if isinstance(results[i], TimeoutError):
                results[i] = Intelligence.INDICATOR_STATUS.INACTIVE.value
        elif isinstance(results[i], (int,float)):
            results[i] = Intelligence.INDICATOR_STATUS.ACTIVE.value
    return results