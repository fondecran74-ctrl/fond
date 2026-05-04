"""Permissions for International Relations."""
from rest_framework.permissions import BasePermission

class CanPartnerInstitution(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
