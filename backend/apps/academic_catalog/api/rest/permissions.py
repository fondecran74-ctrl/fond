"""Permissions for Academic Catalog."""
from rest_framework.permissions import BasePermission

class CanProgram(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
