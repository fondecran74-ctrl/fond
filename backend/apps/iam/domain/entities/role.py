"""Domain entity: Role."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class Role:
    """Domain entity representing a role."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
