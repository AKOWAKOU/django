from rest_framework import serializers
from .models import Todo
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='todo-detail', lookup_field='pk')

    class Meta:
        model = Todo
        fields = ["url", "task", "completed", "timestamp", "updated", "user"]

class UserCreateSerializer(BaseUserSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')

    class Meta(BaseUserSerializer.Meta):
        fields = ['url', 'id', 'email', 'username', 'password']

class CurrentUserSerializer(UserSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')

    class Meta(UserSerializer.Meta):
        fields = ['url', 'id', 'email', 'username', 'password']



