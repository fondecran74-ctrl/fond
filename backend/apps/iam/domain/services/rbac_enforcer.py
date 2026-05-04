"""Rbac Enforcer domain service."""
import structlog

logger = structlog.get_logger(__name__)


class RbacEnforcer:
    """Domain service for rbac enforcer."""

    def evaluate(self, **kwargs) -> bool:
        """Evaluate the policy/rule."""
        raise NotImplementedError
