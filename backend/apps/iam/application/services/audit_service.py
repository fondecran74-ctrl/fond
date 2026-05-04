"""Audit Service service."""
import structlog

logger = structlog.get_logger(__name__)


class AuditService:
    """Service for audit service operations."""

    def __init__(self):
        self.logger = logger
