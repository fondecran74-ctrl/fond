"""User Dto DTO."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class UserDto:
    """Data transfer object for user."""
    id: UUID
    created_at: datetime | None = None
