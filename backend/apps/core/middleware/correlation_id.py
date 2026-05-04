"""Correlation ID middleware."""
import uuid
from django.http import HttpRequest, HttpResponse


class CorrelationIdMiddleware:
    """Attach a unique correlation ID to every request/response."""

    HEADER = "X-Correlation-ID"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        correlation_id = request.headers.get(self.HEADER, str(uuid.uuid4()))
        request.correlation_id = correlation_id  # type: ignore[attr-defined]
        response = self.get_response(request)
        response[self.HEADER] = correlation_id
        return response
