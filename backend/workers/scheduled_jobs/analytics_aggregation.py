"""Analytics Aggregation scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="analytics_aggregation")
def run_analytics_aggregation():
    """Execute analytics aggregation job."""
    logger.info("analytics_aggregation_started")
