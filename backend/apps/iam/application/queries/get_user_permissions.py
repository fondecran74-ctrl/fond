"""Query: Get User Permissions."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetUserPermissionsQuery:
    """Query to get user permissions."""
    user_id: UUID | None = None
