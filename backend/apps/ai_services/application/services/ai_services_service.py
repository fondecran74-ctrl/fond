"""AiServices service."""
import structlog

logger = structlog.get_logger(__name__)


class AiServicesService:
    def __init__(self):
        self.logger = logger
