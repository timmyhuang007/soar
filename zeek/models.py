from enum import Enum, IntEnum
from django.db import models as M

# Create your models here.
class Intelligence(M.Model):
    class INDICATOR_TYPE(Enum):
        ADDR = 'ADDR'
        SUBNET = 'SUBNET'
        URL = 'URL'
        SOFTWARE = 'SOFTWARE'
        EMAIL = 'EMAIL'
        DOMAIN = 'DOMAIN'
        USER_NAME = 'USER_NAME'
        CERT_HASH = 'CERT_HASH'
        PUBKEY_HASH = 'PUBKEY_HASH'
        FILE_HASH = 'FILE_HASH'
    
    INDICATOR_CHOICES = {
        INDICATOR_TYPE.ADDR.value: 'IP',
        INDICATOR_TYPE.SUBNET.value: '网段',
        INDICATOR_TYPE.URL.value: 'URL',
        INDICATOR_TYPE.SOFTWARE.value: '软件名',
        INDICATOR_TYPE.EMAIL.value: '邮箱',
        INDICATOR_TYPE.DOMAIN.value: '域名',
        INDICATOR_TYPE.USER_NAME.value: '用户名',
        INDICATOR_TYPE.CERT_HASH.value: '证书哈希',
        INDICATOR_TYPE.PUBKEY_HASH.value: '公钥哈希',
        INDICATOR_TYPE.FILE_HASH.value: '文件哈希',
    }
    
    class INDICATOR_STATUS(IntEnum):
        UNKNOWN = 0
        ACTIVE = 1
        DELETED = 8
    
    indicator_type = M.CharField(verbose_name='情报类型', choices=INDICATOR_CHOICES.items())
    created = M.DateTimeField(verbose_name='录入时间', blank=True, null=True)
    updated = M.DateTimeField(verbose='更新时间', blank=True, null=True)
    last_active = M.DateTimeField(verbose='最后活跃时间', blank=True, null=True)
    status = M.SmallIntegerField(verbose_name='情报状态', blank=True, null=True, default=INDICATOR_STATUS.UNKNOWN.value)
    source = M.CharField(verbose_name='来源', max_length=64, blank=True, null=True)
    desc = M.TextField(verbose_name='描述', blank=True, null=True)
    link = M.URLField(verbose_name='链接', blank=True, null=True)
    do_notice = M.BooleanField(verbose_name='重点关注', blank=True, null=True)
    
    class Meta:
        abstract = True

class IntelAddr(Intelligence):
    addr = M.GenericIPAddressField(
        verbose_name=Intelligence.INDICATOR_CHOICES[Intelligence.INDICATOR_TYPE.ADDR.value]
    )

class IntelDomain(Intelligence):
    domain = M.CharField(max_length=256,
        verbose_name=Intelligence.INDICATOR_CHOICES[Intelligence.INDICATOR_TYPE.DOMAIN.value]
    )
    resolve_ip = M.GenericIPAddressField(verbose_name='解析IP')