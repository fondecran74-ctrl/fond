"""Library service."""
import structlog

logger = structlog.get_logger(__name__)


class LibraryService:
    def __init__(self):
        self.logger = logger
