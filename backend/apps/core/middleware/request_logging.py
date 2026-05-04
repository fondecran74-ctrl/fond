"""Request/response logging middleware."""
import time
import structlog
from django.http import HttpRequest, HttpResponse

logger = structlog.get_logger(__name__)


class RequestLoggingMiddleware:
    """Log request duration and details."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        start = time.monotonic()
        response = self.get_response(request)
        duration_ms = (time.monotonic() - start) * 1000
        if request.path.startswith("/api/"):
            logger.info(
                "http_request",
                method=request.method,
                path=request.path,
                status=response.status_code,
                duration_ms=round(duration_ms, 2),
                correlation_id=getattr(request, "correlation_id", None),
            )
        return response
