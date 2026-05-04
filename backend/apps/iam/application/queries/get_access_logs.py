"""Query: Get Access Logs."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetAccessLogsQuery:
    """Query to get access logs."""
    user_id: UUID | None = None
