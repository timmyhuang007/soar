from datetime import datetime, date
from ipaddress import ip_address
from django.contrib.auth import User
from django.db import models

# Create your models here.
class Event(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP', protocol='both', unpack_ipv4=True, default=ip_address(0))
    report_time = models.DateTimeField(verbose_name='上报时间', default=datetime.now)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    plan_date = models.DateField(verbose_name='计划日期', default=date.today)
    
