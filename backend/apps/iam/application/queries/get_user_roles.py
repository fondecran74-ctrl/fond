"""Query: Get User Roles."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetUserRolesQuery:
    """Query to get user roles."""
    user_id: UUID | None = None
