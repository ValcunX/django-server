from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

class BearerAuthentication(TokenAuthentication):
    keyword = 'Bearer'

class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            return request.user == obj    
        return request.user == obj.user
