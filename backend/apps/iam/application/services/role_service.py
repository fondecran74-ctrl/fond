"""Role Service service."""
import structlog

logger = structlog.get_logger(__name__)


class RoleService:
    """Service for role service operations."""

    def __init__(self):
        self.logger = logger
