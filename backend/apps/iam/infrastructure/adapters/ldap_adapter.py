"""Ldap Adapter."""
import structlog

logger = structlog.get_logger(__name__)


class LdapAdapter:
    """Adapter for ldap integration."""

    def __init__(self):
        self.logger = logger
