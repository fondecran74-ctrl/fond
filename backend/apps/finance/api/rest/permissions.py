"""Permissions for Finance."""
from rest_framework.permissions import BasePermission

class CanBudget(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
