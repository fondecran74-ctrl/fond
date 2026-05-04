"""InternshipsAlternance service."""
import structlog

logger = structlog.get_logger(__name__)


class InternshipsAlternanceService:
    def __init__(self):
        self.logger = logger
