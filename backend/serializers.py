from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import YoutubeData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class YoutubeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YoutubeData
        fields = '__all__'