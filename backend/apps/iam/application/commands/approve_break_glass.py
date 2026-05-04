"""Command: Approve Break Glass."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ApproveBreakGlassCommand:
    """Command to approve break glass."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
