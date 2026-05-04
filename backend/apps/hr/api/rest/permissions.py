"""Permissions for Human Resources."""
from rest_framework.permissions import BasePermission

class CanEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
