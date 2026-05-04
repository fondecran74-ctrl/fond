"""Permissions for Audit & Traceability."""
from rest_framework.permissions import BasePermission

class CanAuditLog(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
