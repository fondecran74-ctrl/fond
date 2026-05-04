"""AuditTraceability service."""
import structlog

logger = structlog.get_logger(__name__)


class AuditTraceabilityService:
    def __init__(self):
        self.logger = logger
