"""Command: Assign Role."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class AssignRoleCommand:
    """Command to assign role."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
