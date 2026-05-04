"""AnalyticsBi service."""
import structlog

logger = structlog.get_logger(__name__)


class AnalyticsBiService:
    def __init__(self):
        self.logger = logger
