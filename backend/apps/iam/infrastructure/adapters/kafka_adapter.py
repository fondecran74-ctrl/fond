"""Kafka Adapter."""
import structlog

logger = structlog.get_logger(__name__)


class KafkaAdapter:
    """Adapter for kafka integration."""

    def __init__(self):
        self.logger = logger
