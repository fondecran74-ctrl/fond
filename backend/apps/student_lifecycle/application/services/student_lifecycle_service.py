"""StudentLifecycle service."""
import structlog

logger = structlog.get_logger(__name__)


class StudentLifecycleService:
    def __init__(self):
        self.logger = logger
