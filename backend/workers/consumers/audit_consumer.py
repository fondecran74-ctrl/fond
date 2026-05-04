"""Audit Consumer."""
import structlog

logger = structlog.get_logger(__name__)


class AuditConsumer:
    def consume(self):
        logger.info("audit_consumer_started")
