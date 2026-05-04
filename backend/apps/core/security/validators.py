"""Security validators."""
import re


def validate_no_script_injection(value: str) -> bool:
    """Check for potential script injection."""
    patterns = [
        r"<script",
        r"javascript:",
        r"on\w+\s*=",
        r"eval\s*\(",
        r"expression\s*\(",
    ]
    for pattern in patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return False
    return True


def validate_sql_safe(value: str) -> bool:
    """Basic SQL injection check."""
    dangerous = ["--", ";--", "/*", "*/", "xp_", "UNION SELECT", "DROP TABLE", "DELETE FROM"]
    upper = value.upper()
    return not any(d in upper for d in dangerous)
