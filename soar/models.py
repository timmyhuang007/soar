from django.db import models
from django_cryptography.fields import encrypt
from versionfield import VersionField

# Create your models here.
class Environment(models.Model):
    name = models.CharField(verbose_name='环境变量名', max_length=32)
    value = encrypt(models.TextField(verbose_name='环境变量值', max_length=1024))
    version = VersionField(verbose_name='版本', default='0.0', blank=True)

    def __str__(self):
        return f'{self.id:04d}|{self.name}'

