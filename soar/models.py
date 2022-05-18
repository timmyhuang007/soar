from django.db import models
from django_cryptography.fields import encrypt

# Create your models here.
class Environment(models.Model):
    name = models.CharField(verbose_name='环境变量名', max_length=32)
    value = encrypt(models.TextField(verbose_name='环境变量值', max_length=1024))

