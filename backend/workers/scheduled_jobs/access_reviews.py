"""Access Reviews scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="access_reviews")
def run_access_reviews():
    """Execute access reviews job."""
    logger.info("access_reviews_started")
