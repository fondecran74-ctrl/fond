"""Role Exceptions."""
from apps.core.exceptions.base import EMSException


class RoleError(EMSException):
    """Exception for role errors."""
    default_code = "role_error"
