"""Segregation Of Duties domain service."""
import structlog

logger = structlog.get_logger(__name__)


class SegregationOfDuties:
    """Domain service for segregation of duties."""

    def evaluate(self, **kwargs) -> bool:
        """Evaluate the policy/rule."""
        raise NotImplementedError
