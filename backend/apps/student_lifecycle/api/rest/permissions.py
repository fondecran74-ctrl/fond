"""Permissions for Student Lifecycle."""
from rest_framework.permissions import BasePermission

class CanEnrollment(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
