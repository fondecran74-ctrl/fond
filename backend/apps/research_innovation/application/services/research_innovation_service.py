"""ResearchInnovation service."""
import structlog

logger = structlog.get_logger(__name__)


class ResearchInnovationService:
    def __init__(self):
        self.logger = logger
