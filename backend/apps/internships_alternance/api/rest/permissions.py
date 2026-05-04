"""Permissions for Internships & Alternance."""
from rest_framework.permissions import BasePermission

class CanInternshipOffer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
