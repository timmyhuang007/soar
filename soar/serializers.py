from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer
from soar.models import Environment

# Serializers define the API representation.
class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        
class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group

class EnvironmentSerializer(HyperlinkedModelSerializer):
    class Meata:
        model = Environment