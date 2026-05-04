"""Domain entity: User."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class User:
    """Domain entity representing a user."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
