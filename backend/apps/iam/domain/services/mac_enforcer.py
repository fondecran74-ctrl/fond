"""Mac Enforcer domain service."""
import structlog

logger = structlog.get_logger(__name__)


class MacEnforcer:
    """Domain service for mac enforcer."""

    def evaluate(self, **kwargs) -> bool:
        """Evaluate the policy/rule."""
        raise NotImplementedError
