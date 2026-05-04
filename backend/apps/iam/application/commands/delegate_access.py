"""Command: Delegate Access."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class DelegateAccessCommand:
    """Command to delegate access."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
