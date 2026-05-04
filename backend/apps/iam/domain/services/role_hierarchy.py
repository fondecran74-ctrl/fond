"""Role Hierarchy domain service."""
import structlog

logger = structlog.get_logger(__name__)


class RoleHierarchy:
    """Domain service for role hierarchy."""

    def evaluate(self, **kwargs) -> bool:
        """Evaluate the policy/rule."""
        raise NotImplementedError
