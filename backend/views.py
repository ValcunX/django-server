from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import LanguageSerializer, ProjectSerializer, UserSerializer
from .models import Language, Project, User


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
