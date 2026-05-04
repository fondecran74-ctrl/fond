"""Permissions for AI Services."""
from rest_framework.permissions import BasePermission

class CanChatSession(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
