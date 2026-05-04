"""Command: Revoke Role."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class RevokeRoleCommand:
    """Command to revoke role."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
