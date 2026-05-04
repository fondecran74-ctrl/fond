"""Assessments service."""
import structlog

logger = structlog.get_logger(__name__)


class AssessmentsService:
    def __init__(self):
        self.logger = logger
