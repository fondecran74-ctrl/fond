"""Global test fixtures."""
import pytest
from rest_framework.test import APIClient
from apps.iam.infrastructure.orm.models_user import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        email="admin@ems.test",
        username="admin",
        password="SecureP@ss123!",
        first_name="Admin",
        last_name="System",
    )


@pytest.fixture
def authenticated_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client
