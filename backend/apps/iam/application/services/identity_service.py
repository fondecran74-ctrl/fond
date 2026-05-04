"""Identity Service service."""
import structlog

logger = structlog.get_logger(__name__)


class IdentityService:
    """Service for identity service operations."""

    def __init__(self):
        self.logger = logger
