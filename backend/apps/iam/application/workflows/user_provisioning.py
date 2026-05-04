"""User Provisioning workflow."""
import structlog

logger = structlog.get_logger(__name__)


class UserProvisioningWorkflow:
    """Orchestrate the user provisioning process."""

    def execute(self, **kwargs):
        logger.info("user_provisioning_started", **kwargs)
