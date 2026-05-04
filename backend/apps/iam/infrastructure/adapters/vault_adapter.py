"""Vault Adapter."""
import structlog

logger = structlog.get_logger(__name__)


class VaultAdapter:
    """Adapter for vault integration."""

    def __init__(self):
        self.logger = logger
