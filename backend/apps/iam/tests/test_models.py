"""IAM model tests."""
import pytest
from apps.iam.infrastructure.orm.models_user import User


@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="securepassword123!",
            first_name="Test",
            last_name="User",
            user_type="STUDENT",
        )
        assert user.email == "test@example.com"
        assert user.full_name == "Test User"
        assert user.account_status == "PENDING_ACTIVATION"

    def test_no_self_registration_endpoint(self):
        """Verify there is no self-registration capability."""
        assert not hasattr(User.objects, "register")

    def test_provisioning_fields(self):
        user = User.objects.create_user(
            email="prov@example.com",
            username="provuser",
            first_name="Prov",
            last_name="User",
            user_type="STUDENT",
            provisioning_method="MANUAL",
            provisioning_source="Scolarité",
        )
        assert user.provisioning_method == "MANUAL"
        assert user.provisioning_source == "Scolarité"
