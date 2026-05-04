"""Tenant (institution) context middleware."""
import contextvars
from django.http import HttpRequest, HttpResponse

_current_institution_id: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "current_institution_id", default=None
)


def get_current_institution_id() -> str | None:
    """Return the current institution ID from context."""
    return _current_institution_id.get()


class TenantContextMiddleware:
    """Extract and store institution context from request."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        institution_id = request.headers.get("X-Institution-ID")
        if not institution_id and hasattr(request, "user") and hasattr(request.user, "institution_id"):
            institution_id = str(getattr(request.user, "institution_id", None))
        token = _current_institution_id.set(institution_id)
        try:
            return self.get_response(request)
        finally:
            _current_institution_id.reset(token)
