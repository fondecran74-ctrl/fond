"""Finance service."""
import structlog

logger = structlog.get_logger(__name__)


class FinanceService:
    def __init__(self):
        self.logger = logger
