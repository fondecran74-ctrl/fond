"""Command: Create User."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateUserCommand:
    """Command to create user."""
    performed_by: UUID
    email: str
    reason: str = ""
