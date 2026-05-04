"""Permissions for Library."""
from rest_framework.permissions import BasePermission

class CanCatalogItem(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
