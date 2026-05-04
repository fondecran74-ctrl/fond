"""Analytics Consumer."""
import structlog

logger = structlog.get_logger(__name__)


class AnalyticsConsumer:
    def consume(self):
        logger.info("analytics_consumer_started")
