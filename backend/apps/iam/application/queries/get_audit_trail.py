"""Query: Get Audit Trail."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetAuditTrailQuery:
    """Query to get audit trail."""
    user_id: UUID | None = None
