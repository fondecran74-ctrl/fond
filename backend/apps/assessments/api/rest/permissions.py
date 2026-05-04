"""Permissions for Assessments & Grading."""
from rest_framework.permissions import BasePermission

class CanExamination(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
