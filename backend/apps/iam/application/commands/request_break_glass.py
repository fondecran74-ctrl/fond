"""Command: Request Break Glass."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class RequestBreakGlassCommand:
    """Command to request break glass."""
    performed_by: UUID
    user_id: UUID
    reason: str = ""
