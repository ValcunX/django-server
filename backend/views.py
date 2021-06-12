from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import LanguageSerializer, ProjectSerializer, UserSerializer, UserProjectSerializer
from .models import Language, Project


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_context(self):
        context = super(LanguageViewSet, self).get_serializer_context()
        context.update({"request": None})
        return context


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_context(self):
        context = super(ProjectViewSet, self).get_serializer_context()
        context.update({"request": None})
        return context


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_context(self):
        context = super(UserViewSet, self).get_serializer_context()
        context.update({"request": None})
        return context

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        user = self.get_object()
        queryset = Project.objects.filter(user=user)
        serializer = UserProjectSerializer(queryset, many=True, context={'request': None})
        return Response(serializer.data)
