"""String utility functions."""
import re
import unicodedata


def slugify(value: str) -> str:
    """Convert a string to a URL-friendly slug."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def truncate(value: str, length: int = 100) -> str:
    """Truncate a string to the specified length."""
    if len(value) <= length:
        return value
    return value[: length - 3] + "..."
