from rest_framework.serializers import HyperlinkModelSerializer
from seap.models import Event, Comment

class EventSerializer(HyperlinkModelSerializer):
    class Meta:
        model = Event

class CommentSerizlizer(HyperlinkModelSerializer):
    class Meta:
        model = Comment