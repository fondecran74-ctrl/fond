"""Command: Activate Account."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ActivateAccountCommand:
    """Command to activate account."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
