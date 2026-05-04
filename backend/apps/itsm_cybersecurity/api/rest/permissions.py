"""Permissions for ITSM & Cybersecurity."""
from rest_framework.permissions import BasePermission

class CanTicket(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
