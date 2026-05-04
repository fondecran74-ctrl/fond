"""Keycloak Sync scheduled job."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(name="keycloak_sync")
def run_keycloak_sync():
    """Execute keycloak sync job."""
    logger.info("keycloak_sync_started")
