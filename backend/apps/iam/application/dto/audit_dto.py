"""Audit Dto DTO."""
from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AuditDto:
    """Data transfer object for audit."""
    id: UUID
    created_at: datetime | None = None
