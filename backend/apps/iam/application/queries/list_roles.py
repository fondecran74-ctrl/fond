"""Query: List Roles."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ListRolesQuery:
    """Query to list roles."""
    user_id: UUID | None = None
