"""Custom exception handler for DRF."""
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .base import EMSException


def custom_exception_handler(exc, context):
    """Handle exceptions and return standardized error responses."""
    if isinstance(exc, EMSException):
        return Response(
            {
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                }
            },
            status=exc.status_code,
        )

    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            "error": {
                "code": "api_error",
                "message": str(exc),
                "details": response.data if isinstance(response.data, dict) else {"detail": response.data},
            }
        }
    return response
