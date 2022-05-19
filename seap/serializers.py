from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from seap.models import Event, Comment

class EventSerializer(ModelSerializer):
    report_user = PrimaryKeyRelatedField(queryset=User.objects.all())
    comments = StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    event = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'