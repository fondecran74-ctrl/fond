"""Authentication flow integration tests."""
import pytest


@pytest.mark.django_db
@pytest.mark.integration
class TestAuthFlow:
    def test_login_with_valid_credentials(self):
        pass

    def test_login_with_invalid_credentials(self):
        pass

    def test_no_registration_endpoint(self):
        pass
