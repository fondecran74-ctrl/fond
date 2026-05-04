"""CORS configuration utilities."""
from django.conf import settings


def get_cors_origins() -> list[str]:
    """Return allowed CORS origins."""
    return getattr(settings, "CORS_ALLOWED_ORIGINS", [])
