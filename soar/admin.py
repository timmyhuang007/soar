from django.contrib import admin
from soar.models import Environment
from zeek.models import IntelAddr, IntelDomain

# Register your models here.
admin.site.register([Environment, IntelAddr, IntelDomain])