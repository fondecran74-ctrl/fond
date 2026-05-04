"""Date/time utility functions."""
from datetime import date, datetime, timezone


def now_utc() -> datetime:
    """Return the current UTC datetime."""
    return datetime.now(timezone.utc)


def academic_year_for_date(d: date | None = None) -> str:
    """Return the academic year string (e.g. '2025-2026')."""
    d = d or date.today()
    if d.month >= 9:
        return f"{d.year}-{d.year + 1}"
    return f"{d.year - 1}-{d.year}"
