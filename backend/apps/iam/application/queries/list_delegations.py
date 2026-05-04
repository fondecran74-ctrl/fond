"""Query: List Delegations."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ListDelegationsQuery:
    """Query to list delegations."""
    user_id: UUID | None = None
