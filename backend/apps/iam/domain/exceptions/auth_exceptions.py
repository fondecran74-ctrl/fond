"""Auth Exceptions."""
from apps.core.exceptions.base import EMSException


class AuthError(EMSException):
    """Exception for auth errors."""
    default_code = "auth_error"
