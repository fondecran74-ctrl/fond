"""Role Revocation workflow."""
import structlog

logger = structlog.get_logger(__name__)


class RoleRevocationWorkflow:
    """Orchestrate the role revocation process."""

    def execute(self, **kwargs):
        logger.info("role_revocation_started", **kwargs)
