"""IAM-specific permissions."""
from rest_framework.permissions import BasePermission


class IsProvisioningAgent(BasePermission):
    """Only allows provisioning agents (admins, HR, scolarité) to create users."""
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user.is_authenticated and request.user.user_type in (
            "SYSTEM_ADMIN", "FUNCTIONAL_DIRECTOR", "OPERATIONAL_MANAGER", "OPERATOR"
        )


class CanManageRoles(BasePermission):
    """Only allows role managers to modify roles."""
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.user_type in (
            "SYSTEM_ADMIN", "GOVERNANCE"
        )
