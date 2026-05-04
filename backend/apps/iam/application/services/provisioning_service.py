"""Provisioning Service service."""
import structlog

logger = structlog.get_logger(__name__)


class ProvisioningService:
    """Service for provisioning service operations."""

    def __init__(self):
        self.logger = logger
