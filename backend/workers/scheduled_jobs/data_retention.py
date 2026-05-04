"""Data Retention scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="data_retention")
def run_data_retention():
    """Execute data retention job."""
    logger.info("data_retention_started")
