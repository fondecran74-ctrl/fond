"""Opa Adapter."""
import structlog

logger = structlog.get_logger(__name__)


class OpaAdapter:
    """Adapter for opa integration."""

    def __init__(self):
        self.logger = logger
