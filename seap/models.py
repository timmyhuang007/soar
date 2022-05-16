from django.contrib.auth import User
from django.db import models

# Create your models here.
class Event(models.Model):
    ip = models.IPAddressField()

