"""Permissions for Quality, Compliance & Risk."""
from rest_framework.permissions import BasePermission

class CanAccreditation(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
