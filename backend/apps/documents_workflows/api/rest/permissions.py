"""Permissions for Documents & Workflows."""
from rest_framework.permissions import BasePermission

class CanDocument(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
