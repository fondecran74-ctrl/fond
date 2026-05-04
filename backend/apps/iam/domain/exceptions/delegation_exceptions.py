"""Delegation Exceptions."""
from apps.core.exceptions.base import EMSException


class DelegationError(EMSException):
    """Exception for delegation errors."""
    default_code = "delegation_error"
