from rest_framework.serializers import ModelSerializer
from seap.models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event