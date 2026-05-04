"""FacilitiesServices service."""
import structlog

logger = structlog.get_logger(__name__)


class FacilitiesServicesService:
    def __init__(self):
        self.logger = logger
