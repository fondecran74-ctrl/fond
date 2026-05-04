"""OrgStructure service."""
import structlog

logger = structlog.get_logger(__name__)


class OrgStructureService:
    def __init__(self):
        self.logger = logger
