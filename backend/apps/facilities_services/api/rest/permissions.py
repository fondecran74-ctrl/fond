"""Permissions for Facilities & Services."""
from rest_framework.permissions import BasePermission

class CanBuilding(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
