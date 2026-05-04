"""Delegation Workflow workflow."""
import structlog

logger = structlog.get_logger(__name__)


class DelegationWorkflowWorkflow:
    """Orchestrate the delegation workflow process."""

    def execute(self, **kwargs):
        logger.info("delegation_workflow_started", **kwargs)
