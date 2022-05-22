from datetime import datetime, date
from enum import IntEnum
from django.contrib.auth.models import User
from django.db import models as M

# Create your models here.
class Event(M.Model):
    class STATUS(IntEnum):
        IGNORED = -1
        TODO = 0
        DOING = 1
        CLOSED = 2
    STATUS_CHOICES = [
        (STATUS.IGNORED.value, '已忽略'),
        (STATUS.TODO.value, '待响应'),
        (STATUS.DOING.value, '处理中'),
        (STATUS.CLOSED.value, '已关闭'),
    ]

    ip = M.GenericIPAddressField(verbose_name='IP', protocol='both', unpack_ipv4=True, default='0.0.0.0')
    status = M.SmallIntegerField(verbose_name='事件状态', default=STATUS.TODO.value, choices=STATUS_CHOICES)
    report_user = M.ForeignKey(User, verbose_name='上报人', on_delete=M.SET_NULL, blank=True, null=True)
    report_time = M.DateTimeField(verbose_name='上报时间', default=datetime.now)
    plan_date = M.DateField(verbose_name='计划日期', default=date.today)
    title = M.CharField(verbose_name='事件标题', max_length=64)
    url = M.URLField(verbose_name='来源链接', max_length=256, blank=True, null=True)
    screen_shot = M.ImageField(verbose_name='截屏', upload_to='screen_shot/%Y%m%d', max_length=256, blank=True, null=True)
    evidence = M.FileField(verbose_name='证据文件', upload_to='evidence/%Y%m%d', max_length=256, blank=True, null=True)
    extension = M.JSONField(verbose_name='拓展信息', blank=True, null=True)

    def __str__(self):
        return f'{self.id:04d}|{self.title}'

class Comment(M.Model):
    event = M.ForeignKey(Event, on_delete=M.CASCADE, related_name='comments')
    content = M.TextField(verbose_name='评论')
    update_time = M.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return f'{self.id:04d}|{self.event.id:04d}|{self.content}'
