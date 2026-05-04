"""Domain entity: Break Glass Request."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class BreakGlassRequest:
    """Domain entity representing a break glass request."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
