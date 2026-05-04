"""Common validators for the EMS platform."""
import re
from django.core.exceptions import ValidationError


def validate_phone_number(value: str) -> None:
    """Validate international phone number format."""
    pattern = r"^\+?[1-9]\d{1,14}$"
    if not re.match(pattern, value):
        raise ValidationError(f"{value} is not a valid phone number.")


def validate_institutional_email(value: str) -> None:
    """Validate that an email belongs to an institutional domain."""
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
        raise ValidationError(f"{value} is not a valid email address.")
