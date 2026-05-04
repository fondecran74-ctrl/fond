"""Standardized API response wrapper."""
from rest_framework.response import Response


class ApiResponse(Response):
    """Standardized success response."""

    def __init__(self, data=None, message: str = "Success", status: int = 200, **kwargs):
        payload = {
            "status": "success",
            "message": message,
            "data": data,
        }
        super().__init__(data=payload, status=status, **kwargs)
