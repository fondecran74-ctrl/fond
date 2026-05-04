"""Admissions service."""
import structlog

logger = structlog.get_logger(__name__)


class AdmissionsService:
    def __init__(self):
        self.logger = logger
