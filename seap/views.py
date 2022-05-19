from rest_framework.viewsets import ModelViewSet
from seap.models import Event, Comment
from seap.serializers import EventSerializer, CommentSerializer

# ViewSets define the view behavior.
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
