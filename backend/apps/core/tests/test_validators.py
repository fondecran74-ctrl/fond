"""Validator tests."""
import pytest
from django.core.exceptions import ValidationError
from apps.core.validators import validate_phone_number


class TestPhoneValidator:
    def test_valid_phone(self):
        validate_phone_number("+33612345678")

    def test_invalid_phone(self):
        with pytest.raises(ValidationError):
            validate_phone_number("not-a-phone")
