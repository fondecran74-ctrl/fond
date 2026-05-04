"""Abac Enforcer domain service."""
import structlog

logger = structlog.get_logger(__name__)


class AbacEnforcer:
    """Domain service for abac enforcer."""

    def evaluate(self, **kwargs) -> bool:
        """Evaluate the policy/rule."""
        raise NotImplementedError
