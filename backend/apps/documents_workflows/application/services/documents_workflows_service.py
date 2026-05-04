"""DocumentsWorkflows service."""
import structlog

logger = structlog.get_logger(__name__)


class DocumentsWorkflowsService:
    def __init__(self):
        self.logger = logger
