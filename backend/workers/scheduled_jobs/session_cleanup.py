"""Session Cleanup scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="session_cleanup")
def run_session_cleanup():
    """Execute session cleanup job."""
    logger.info("session_cleanup_started")
