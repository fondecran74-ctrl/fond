"""Domain entity: Audit Entry."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class AuditEntry:
    """Domain entity representing a audit entry."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
