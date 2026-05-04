"""Authorization Pipeline domain service."""
import structlog

logger = structlog.get_logger(__name__)


class AuthorizationPipeline:
    """Domain service for authorization pipeline."""

    def evaluate(self, **kwargs) -> bool:
        """Evaluate the policy/rule."""
        raise NotImplementedError
