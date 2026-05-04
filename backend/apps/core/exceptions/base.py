"""Base exception classes for EMS platform."""


class EMSException(Exception):
    """Base exception for all EMS domain errors."""

    default_code = "ems_error"
    default_message = "An error occurred."
    status_code = 500

    def __init__(self, message: str | None = None, code: str | None = None):
        self.message = message or self.default_message
        self.code = code or self.default_code
        super().__init__(self.message)


class ValidationError(EMSException):
    default_code = "validation_error"
    default_message = "Validation failed."
    status_code = 400


class NotFoundError(EMSException):
    default_code = "not_found"
    default_message = "Resource not found."
    status_code = 404


class PermissionDeniedError(EMSException):
    default_code = "permission_denied"
    default_message = "Permission denied."
    status_code = 403


class ConflictError(EMSException):
    default_code = "conflict"
    default_message = "Resource conflict."
    status_code = 409
