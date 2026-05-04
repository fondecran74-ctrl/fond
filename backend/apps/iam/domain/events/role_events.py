"""Role Events events."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class RoleEventsEvent:
    """Domain event for role."""
    event_id: UUID
    occurred_at: datetime
    actor_id: UUID
