"""Domain entity: Permission."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class Permission:
    """Domain entity representing a permission."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
