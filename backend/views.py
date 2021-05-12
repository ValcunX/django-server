from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import LanguageSerializer, ProjectSerializer, UserSerializer
from .models import Language, Project, User


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        user = self.get_object()
        queryset = Project.objects.filter(user=user)
        serializer = ProjectSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
