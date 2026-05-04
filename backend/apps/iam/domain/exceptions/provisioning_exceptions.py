"""Provisioning Exceptions."""
from apps.core.exceptions.base import EMSException


class ProvisioningError(EMSException):
    """Exception for provisioning errors."""
    default_code = "provisioning_error"
