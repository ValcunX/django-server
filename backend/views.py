from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_psq import PsqMixin, Rule

from .serializers import LanguageSerializer, ProjectSerializer, UserSerializer, UserProjectSerializer
from .models import Language, Project
from .authentication import IsSelf

class LanguageViewSet(PsqMixin, viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAdminUser]

    psq_rules = {
        ('list'): [
            Rule([IsAuthenticated], LanguageSerializer),
        ]
    }

    def get_serializer_context(self):
        context = super(LanguageViewSet, self).get_serializer_context()
        context.update({"request": None})
        return context


class ProjectViewSet(PsqMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = [IsAdminUser]

    psq_rules = {
        ('list'): [
            Rule([IsAdminUser], ProjectSerializer),
            Rule([IsAuthenticated], ProjectSerializer,
                    lambda self: Project.objects.filter(user=self.request.user)
                ),
        ],
        ('create', 'retrieve', 'update', 'partial_update', 'destroy'): [
            Rule([IsAdminUser], ProjectSerializer),
            Rule([IsAuthenticated & IsSelf], ProjectSerializer),
        ]
    }

    def get_serializer_context(self):
        context = super(ProjectViewSet, self).get_serializer_context()
        context.update({"request": None})
        return context


class UserViewSet(PsqMixin, viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAdminUser]

    psq_rules = {
        ('list'): [
            Rule([IsAdminUser], UserSerializer),
            Rule([IsAuthenticated], UserSerializer,
                    lambda self: get_user_model().objects.filter(id=self.request.user.id)
                ),
        ],
        ('retrieve', 'update', 'partial_update'): [
            Rule([IsAdminUser], UserSerializer),
            Rule([IsAuthenticated & IsSelf], UserSerializer),
        ],
        ('projects'): [
            Rule([IsAdminUser], UserProjectSerializer),
            Rule([IsAuthenticated & IsSelf], UserProjectSerializer)
        ]
    }

    def get_serializer_context(self):
        context = super(UserViewSet, self).get_serializer_context()
        context.update({"request": None})
        return context

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        user = self.get_object()
        queryset = Project.objects.filter(user=user)
        serializer = UserProjectSerializer(
            queryset, many=True, context={'request': None})
        return Response(serializer.data)
