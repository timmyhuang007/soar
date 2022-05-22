from django.contrib.auth.models import User, Group
from rest_framework import serializers as S
from soar.models import Environment

# Serializers define the API representation.
class UserSerializer(S.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','is_superuser','username','first_name','last_name','email','is_staff','is_active']
        
class GroupSerializer(S.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class EnvironmentSerializer(S.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'