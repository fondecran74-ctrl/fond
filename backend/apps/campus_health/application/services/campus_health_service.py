"""CampusHealth service."""
import structlog

logger = structlog.get_logger(__name__)


class CampusHealthService:
    def __init__(self):
        self.logger = logger
