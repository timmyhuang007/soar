from rest_framework.serializers import ModelSerializer
from seap.models import Event, Comment

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event

class CommentSerizlizer(ModelSerializer):
    class Meta:
        model = Comment