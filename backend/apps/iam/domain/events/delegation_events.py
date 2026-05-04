"""Delegation Events events."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class DelegationEventsEvent:
    """Domain event for delegation."""
    event_id: UUID
    occurred_at: datetime
    actor_id: UUID
