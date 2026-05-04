"""Vault Client."""
import structlog
from django.conf import settings

logger = structlog.get_logger(__name__)


class VaultClient:
    """Client for vault client."""

    def __init__(self):
        self.logger = logger
