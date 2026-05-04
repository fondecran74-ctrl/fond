"""Governance service."""
import structlog

logger = structlog.get_logger(__name__)


class GovernanceService:
    def __init__(self):
        self.logger = logger
