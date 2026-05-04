"""Event Consumers."""
import structlog

logger = structlog.get_logger(__name__)


class EventConsumers:
    def consume(self):
        logger.info("event_consumers_started")
