"""Mfa Service service."""
import structlog

logger = structlog.get_logger(__name__)


class MfaService:
    """Service for mfa service operations."""

    def __init__(self):
        self.logger = logger
