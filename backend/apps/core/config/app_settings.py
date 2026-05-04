"""Application-level settings."""
from django.conf import settings


class AppSettings:
    """Centralized application settings."""

    MAX_PAGE_SIZE = getattr(settings, "MAX_PAGE_SIZE", 100)
    DEFAULT_PAGE_SIZE = getattr(settings, "DEFAULT_PAGE_SIZE", 25)
    AUDIT_ENABLED = getattr(settings, "AUDIT_ENABLED", True)
    ENCRYPTION_KEY_ID = getattr(settings, "ENCRYPTION_KEY_ID", "ems-master-key")
    MAX_UPLOAD_SIZE_MB = getattr(settings, "MAX_UPLOAD_SIZE_MB", 50)


app_settings = AppSettings()
