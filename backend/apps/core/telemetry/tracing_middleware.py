"""OpenTelemetry tracing middleware."""
from django.http import HttpRequest, HttpResponse
from .tracing import tracer


class TracingMiddleware:
    """Add OpenTelemetry spans to requests."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        with tracer.start_as_current_span(
            f"{request.method} {request.path}",
            attributes={
                "http.method": request.method,
                "http.url": request.build_absolute_uri(),
            },
        ):
            response = self.get_response(request)
            return response
