"""Casbin Adapter."""
import structlog

logger = structlog.get_logger(__name__)


class CasbinAdapter:
    """Adapter for casbin integration."""

    def __init__(self):
        self.logger = logger
