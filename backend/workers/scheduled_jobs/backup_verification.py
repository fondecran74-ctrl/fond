"""Backup Verification scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="backup_verification")
def run_backup_verification():
    """Execute backup verification job."""
    logger.info("backup_verification_started")
