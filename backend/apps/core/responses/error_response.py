"""Standardized error response."""
from rest_framework.response import Response


class ErrorResponse(Response):
    """Standardized error response."""

    def __init__(self, message: str, code: str = "error", status: int = 400, errors=None, **kwargs):
        payload = {
            "status": "error",
            "error": {
                "code": code,
                "message": message,
            },
        }
        if errors:
            payload["error"]["details"] = errors
        super().__init__(data=payload, status=status, **kwargs)
