"""Permission Dto DTO."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class PermissionDto:
    """Data transfer object for permission."""
    id: UUID
    created_at: datetime | None = None
