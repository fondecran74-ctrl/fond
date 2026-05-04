"""Notification Consumer."""
import structlog

logger = structlog.get_logger(__name__)


class NotificationConsumer:
    def consume(self):
        logger.info("notification_consumer_started")
