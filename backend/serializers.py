from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Language, Project, User

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'image_id')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'user', 'language', 'volume_id', 'last_mdate')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')

class UserProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'user', 'language', 'volume_id', 'last_mdate')
        depth = 1