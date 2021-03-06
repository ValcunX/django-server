from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Language, Project


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'image_id', 'url')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'user', 'language', 'volume_id', 'last_mdate', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'url')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')


class UserProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    language = LanguageSerializer()

    class Meta:
        model = Project
        fields = ('id', 'name', 'user', 'language', 'volume_id', 'last_mdate')
        depth = 1
