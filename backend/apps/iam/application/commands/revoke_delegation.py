"""Command: Revoke Delegation."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class RevokeDelegationCommand:
    """Command to revoke delegation."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
