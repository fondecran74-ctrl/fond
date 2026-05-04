"""Casbin Enforcer."""
import structlog
from django.conf import settings

logger = structlog.get_logger(__name__)


class CasbinEnforcer:
    """Client for casbin enforcer."""

    def __init__(self):
        self.logger = logger
