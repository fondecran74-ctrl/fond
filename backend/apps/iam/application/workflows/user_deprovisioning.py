"""User Deprovisioning workflow."""
import structlog

logger = structlog.get_logger(__name__)


class UserDeprovisioningWorkflow:
    """Orchestrate the user deprovisioning process."""

    def execute(self, **kwargs):
        logger.info("user_deprovisioning_started", **kwargs)
