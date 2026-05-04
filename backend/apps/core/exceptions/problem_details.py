"""RFC 7807 Problem Details responses."""
from dataclasses import dataclass


@dataclass
class ProblemDetail:
    """RFC 7807 Problem Details representation."""
    type: str
    title: str
    status: int
    detail: str
    instance: str = ""

    def to_dict(self) -> dict:
        result = {
            "type": self.type,
            "title": self.title,
            "status": self.status,
            "detail": self.detail,
        }
        if self.instance:
            result["instance"] = self.instance
        return result
