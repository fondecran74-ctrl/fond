"""QualityComplianceRisk service."""
import structlog

logger = structlog.get_logger(__name__)


class QualityComplianceRiskService:
    def __init__(self):
        self.logger = logger
