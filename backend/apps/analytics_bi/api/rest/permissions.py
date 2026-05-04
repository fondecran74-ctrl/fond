"""Permissions for Analytics & BI."""
from rest_framework.permissions import BasePermission

class CanDashboard(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
