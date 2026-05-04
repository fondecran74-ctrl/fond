"""Permissions for Notifications & Communication."""
from rest_framework.permissions import BasePermission

class CanNotification(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
