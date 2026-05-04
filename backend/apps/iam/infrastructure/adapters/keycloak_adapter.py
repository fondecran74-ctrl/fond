"""Keycloak Adapter."""
import structlog

logger = structlog.get_logger(__name__)


class KeycloakAdapter:
    """Adapter for keycloak integration."""

    def __init__(self):
        self.logger = logger
