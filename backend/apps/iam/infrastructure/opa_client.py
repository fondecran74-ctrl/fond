"""Opa Client."""
import structlog
from django.conf import settings

logger = structlog.get_logger(__name__)


class OpaClient:
    """Client for opa client."""

    def __init__(self):
        self.logger = logger
