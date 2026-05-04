"""Break Glass Events events."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class BreakGlassEventsEvent:
    """Domain event for break glass."""
    event_id: UUID
    occurred_at: datetime
    actor_id: UUID
