"""Access Review Service service."""
import structlog

logger = structlog.get_logger(__name__)


class AccessReviewService:
    """Service for access review service operations."""

    def __init__(self):
        self.logger = logger
