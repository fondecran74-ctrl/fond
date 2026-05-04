"""Break Glass Activation workflow."""
import structlog

logger = structlog.get_logger(__name__)


class BreakGlassActivationWorkflow:
    """Orchestrate the break glass activation process."""

    def execute(self, **kwargs):
        logger.info("break_glass_activation_started", **kwargs)
