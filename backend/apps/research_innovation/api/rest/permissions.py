"""Permissions for Research & Innovation."""
from rest_framework.permissions import BasePermission

class CanResearchProject(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
