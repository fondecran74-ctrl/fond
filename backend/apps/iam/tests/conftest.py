"""IAM test fixtures."""
import pytest
from apps.iam.infrastructure.orm.models_user import User


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        email="admin@ems.test",
        username="admin",
        password="Test1234!@#$",
        first_name="Admin",
        last_name="System",
    )


@pytest.fixture
def regular_user(db):
    return User.objects.create_user(
        email="user@ems.test",
        username="testuser",
        password="Test1234!@#$",
        first_name="Test",
        last_name="User",
        user_type="STUDENT",
    )
