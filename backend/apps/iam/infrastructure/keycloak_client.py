"""Keycloak Client."""
import structlog
from django.conf import settings

logger = structlog.get_logger(__name__)


class KeycloakClient:
    """Client for keycloak client."""

    def __init__(self):
        self.logger = logger
