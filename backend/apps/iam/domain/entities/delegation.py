"""Domain entity: Delegation."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class Delegation:
    """Domain entity representing a delegation."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
