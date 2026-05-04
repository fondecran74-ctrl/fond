"""Identifier generation utilities."""
import uuid
import hashlib
import time


def generate_uuid() -> str:
    """Generate a UUID v4."""
    return str(uuid.uuid4())


def generate_short_id(prefix: str = "") -> str:
    """Generate a short unique identifier."""
    ts = str(time.time()).encode()
    h = hashlib.sha256(ts + uuid.uuid4().bytes).hexdigest()[:8]
    return f"{prefix}{h}" if prefix else h


def generate_student_id(institution_code: str, year: int, sequence: int) -> str:
    """Generate a student identifier."""
    return f"{institution_code}{year}{sequence:05d}"
