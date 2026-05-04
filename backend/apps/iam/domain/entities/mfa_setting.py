"""Domain entity: Mfa Setting."""
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass
class MfaSetting:
    """Domain entity representing a mfa setting."""
    id: UUID
    created_at: datetime = field(default_factory=datetime.now)
