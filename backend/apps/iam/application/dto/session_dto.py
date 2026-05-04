"""Session Dto DTO."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class SessionDto:
    """Data transfer object for session."""
    id: UUID
    created_at: datetime | None = None
