"""IAM API view tests."""
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUserAPI:
    def test_unauthenticated_user_cannot_list_users(self):
        client = APIClient()
        response = client.get("/api/v1/iam/users/")
        assert response.status_code in (401, 403)

    def test_no_register_endpoint_exists(self):
        """Ensure no registration endpoint exists."""
        client = APIClient()
        for path in ["/api/v1/iam/register/", "/api/v1/iam/signup/", "/api/v1/iam/create-account/"]:
            response = client.post(path, {})
            assert response.status_code == 404
