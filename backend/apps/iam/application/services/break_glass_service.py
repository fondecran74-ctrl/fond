"""Break Glass Service service."""
import structlog

logger = structlog.get_logger(__name__)


class BreakGlassService:
    """Service for break glass service operations."""

    def __init__(self):
        self.logger = logger
