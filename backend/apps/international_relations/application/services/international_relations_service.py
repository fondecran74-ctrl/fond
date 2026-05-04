"""InternationalRelations service."""
import structlog

logger = structlog.get_logger(__name__)


class InternationalRelationsService:
    def __init__(self):
        self.logger = logger
