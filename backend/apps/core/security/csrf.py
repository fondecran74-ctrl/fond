"""CSRF utilities."""
from django.middleware.csrf import get_token
from django.http import HttpRequest


def get_csrf_token(request: HttpRequest) -> str:
    """Return the CSRF token for the current request."""
    return get_token(request)
