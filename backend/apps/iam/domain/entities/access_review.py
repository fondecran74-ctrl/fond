"""Domain entity: Access Review."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class AccessReview:
    """Domain entity representing a access review."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
