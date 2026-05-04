"""Role Assignment workflow."""
import structlog

logger = structlog.get_logger(__name__)


class RoleAssignmentWorkflow:
    """Orchestrate the role assignment process."""

    def execute(self, **kwargs):
        logger.info("role_assignment_started", **kwargs)
