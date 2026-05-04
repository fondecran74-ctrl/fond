"""Domain entity: Session."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class Session:
    """Domain entity representing a session."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
