"""Access Exceptions."""
from apps.core.exceptions.base import EMSException


class AccessError(EMSException):
    """Exception for access errors."""
    default_code = "access_error"
