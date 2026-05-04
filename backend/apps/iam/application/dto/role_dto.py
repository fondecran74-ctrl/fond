"""Role Dto DTO."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class RoleDto:
    """Data transfer object for role."""
    id: UUID
    created_at: datetime | None = None
