"""Session Service service."""
import structlog

logger = structlog.get_logger(__name__)


class SessionService:
    """Service for session service operations."""

    def __init__(self):
        self.logger = logger
