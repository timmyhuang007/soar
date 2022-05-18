from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from soar.models import Environment
from soar.serializers import UserSerializer, GroupSerializer, EnvironmentSerializer

# ViewSets define the view behavior.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EnvironmentViewSet(ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer