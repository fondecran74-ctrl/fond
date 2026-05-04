"""Command: Deactivate Account."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeactivateAccountCommand:
    """Command to deactivate account."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
