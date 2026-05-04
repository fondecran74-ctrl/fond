"""Command: Provision Identity."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ProvisionIdentityCommand:
    """Command to provision identity."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
