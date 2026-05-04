"""Access Review workflow."""
import structlog

logger = structlog.get_logger(__name__)


class AccessReviewWorkflow:
    """Orchestrate the access review process."""

    def execute(self, **kwargs):
        logger.info("access_review_started", **kwargs)
