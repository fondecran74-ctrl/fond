"""Audit logging middleware."""
import structlog
from django.http import HttpRequest, HttpResponse

logger = structlog.get_logger(__name__)


class AuditMiddleware:
    """Log all API requests for audit purposes."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        if request.path.startswith("/api/"):
            logger.info(
                "api_request",
                method=request.method,
                path=request.path,
                status=response.status_code,
                user=getattr(request.user, "id", None),
            )
        return response
