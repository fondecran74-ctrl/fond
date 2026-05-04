"""Break Glass Exceptions."""
from apps.core.exceptions.base import EMSException


class BreakGlassError(EMSException):
    """Exception for break glass errors."""
    default_code = "break_glass_error"
