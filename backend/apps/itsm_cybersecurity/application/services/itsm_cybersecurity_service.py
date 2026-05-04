"""ItsmCybersecurity service."""
import structlog

logger = structlog.get_logger(__name__)


class ItsmCybersecurityService:
    def __init__(self):
        self.logger = logger
