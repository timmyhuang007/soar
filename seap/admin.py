from django.contrib import admin
from seap.models import Event, Comment

# Register your models here.
admin.site.register([Event, Comment])
