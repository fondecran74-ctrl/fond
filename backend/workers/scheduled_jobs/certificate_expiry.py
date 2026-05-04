"""Certificate Expiry scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="certificate_expiry")
def run_certificate_expiry():
    """Execute certificate expiry job."""
    logger.info("certificate_expiry_started")
