"""Session Events events."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class SessionEventsEvent:
    """Domain event for session."""
    event_id: UUID
    occurred_at: datetime
    actor_id: UUID
