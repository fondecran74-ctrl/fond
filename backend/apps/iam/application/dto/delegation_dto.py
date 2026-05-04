"""Delegation Dto DTO."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class DelegationDto:
    """Data transfer object for delegation."""
    id: UUID
    created_at: datetime | None = None
