"""Delegation Service service."""
import structlog

logger = structlog.get_logger(__name__)


class DelegationService:
    """Service for delegation service operations."""

    def __init__(self):
        self.logger = logger
