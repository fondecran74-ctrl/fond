"""Input sanitization utilities."""
import bleach


ALLOWED_TAGS = ["b", "i", "u", "em", "strong", "p", "br", "ul", "ol", "li", "a", "h1", "h2", "h3"]
ALLOWED_ATTRIBUTES = {"a": ["href", "title"]}


def sanitize_html(value: str) -> str:
    """Sanitize HTML input."""
    return bleach.clean(value, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)


def sanitize_text(value: str) -> str:
    """Strip all HTML tags from input."""
    return bleach.clean(value, tags=[], strip=True)
