"""Request context middleware."""
import contextvars
from django.http import HttpRequest, HttpResponse

_current_request: contextvars.ContextVar[HttpRequest | None] = contextvars.ContextVar(
    "current_request", default=None
)


def get_current_request() -> HttpRequest | None:
    """Return the current request from context."""
    return _current_request.get()


class RequestContextMiddleware:
    """Store the current request in a context variable."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        token = _current_request.set(request)
        try:
            return self.get_response(request)
        finally:
            _current_request.reset(token)
