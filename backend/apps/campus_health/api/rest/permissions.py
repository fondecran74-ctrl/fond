"""Permissions for Campus Health."""
from rest_framework.permissions import BasePermission

class CanMedicalRecord(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
