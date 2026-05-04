"""Query: Check Access."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class CheckAccessQuery:
    """Query to check access."""
    user_id: UUID | None = None
