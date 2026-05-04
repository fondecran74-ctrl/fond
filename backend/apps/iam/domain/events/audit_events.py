"""Audit Events events."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AuditEventsEvent:
    """Domain event for audit."""
    event_id: UUID
    occurred_at: datetime
    actor_id: UUID
