"""User and identity models."""
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.core.abstract_models import TimestampedModel
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    """EMS User — provisioned exclusively by the institution."""

    class ProvisioningMethod(models.TextChoices):
        MANUAL = "MANUAL", "Manual creation"
        IMPORT_CSV = "IMPORT_CSV", "CSV import"
        API_INTEGRATION = "API_INTEGRATION", "API integration"
        BULK_IMPORT = "BULK_IMPORT", "Bulk import"
        KEYCLOAK_SYNC = "KEYCLOAK_SYNC", "Keycloak synchronization"

    class UserType(models.TextChoices):
        SYSTEM_ADMIN = "SYSTEM_ADMIN", "System Administrator"
        GOVERNANCE = "GOVERNANCE", "Governance"
        DIRECTOR = "DIRECTOR", "Director"
        FUNCTIONAL_DIRECTOR = "FUNCTIONAL_DIRECTOR", "Functional Director"
        OPERATIONAL_MANAGER = "OPERATIONAL_MANAGER", "Operational Manager"
        OPERATOR = "OPERATOR", "Operator/Technician"
        TEACHER = "TEACHER", "Teacher"
        RESEARCHER = "RESEARCHER", "Researcher"
        STUDENT = "STUDENT", "Student"
        CANDIDATE = "CANDIDATE", "Candidate"
        PARENT = "PARENT", "Parent/Guardian"
        ALUMNI = "ALUMNI", "Alumni"
        PARTNER = "PARTNER", "Partner"
        SERVICE_ACCOUNT = "SERVICE_ACCOUNT", "Service Account"

    class AccountStatus(models.TextChoices):
        PENDING_ACTIVATION = "PENDING_ACTIVATION", "Pending activation"
        ACTIVE = "ACTIVE", "Active"
        SUSPENDED = "SUSPENDED", "Suspended"
        LOCKED = "LOCKED", "Locked"
        DEACTIVATED = "DEACTIVATED", "Deactivated"
        ARCHIVED = "ARCHIVED", "Archived"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_type = models.CharField(max_length=30, choices=UserType.choices)
    account_status = models.CharField(
        max_length=25, choices=AccountStatus.choices, default=AccountStatus.PENDING_ACTIVATION
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Provisioning — NO self-registration
    provisioning_method = models.CharField(
        max_length=20, choices=ProvisioningMethod.choices, default=ProvisioningMethod.MANUAL
    )
    provisioning_source = models.CharField(max_length=255, blank=True, default="")
    provisioned_by = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="provisioned_users"
    )
    provisioned_at = models.DateTimeField(auto_now_add=True)

    # Institution scope
    institution = models.ForeignKey(
        "org_structure.Institution", on_delete=models.CASCADE, null=True, blank=True, related_name="users"
    )

    # Keycloak integration
    keycloak_id = models.CharField(max_length=255, blank=True, default="", db_index=True)

    # Security
    failed_login_attempts = models.PositiveIntegerField(default=0)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    password_changed_at = models.DateTimeField(null=True, blank=True)
    must_change_password = models.BooleanField(default=True)
    activation_token = models.CharField(max_length=255, blank=True, default="")
    activation_token_expires = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    class Meta:
        db_table = "iam_users"
        ordering = ["-created_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"
        indexes = [
            models.Index(fields=["user_type"]),
            models.Index(fields=["account_status"]),
            models.Index(fields=["institution"]),
        ]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def lock_account(self) -> None:
        self.account_status = self.AccountStatus.LOCKED
        self.save(update_fields=["account_status", "updated_at"])

    def activate_account(self) -> None:
        self.account_status = self.AccountStatus.ACTIVE
        self.must_change_password = False
        self.save(update_fields=["account_status", "must_change_password", "updated_at"])


class Identity(TimestampedModel):
    """Physical person identity, distinct from the user account."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="identity")
    national_id = models.CharField(max_length=50, blank=True, default="")
    passport_number = models.CharField(max_length=50, blank=True, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True, default="")
    nationality = models.CharField(max_length=100, blank=True, default="")
    gender = models.CharField(max_length=20, blank=True, default="")
    photo_url = models.URLField(blank=True, default="")
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="verified_identities"
    )

    class Meta:
        db_table = "iam_identities"
        verbose_name = "Identity"
        verbose_name_plural = "Identities"


class UserProfile(TimestampedModel):
    """Extended user profile information."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True, default="")
    secondary_email = models.EmailField(blank=True, default="")
    address_line_1 = models.CharField(max_length=255, blank=True, default="")
    address_line_2 = models.CharField(max_length=255, blank=True, default="")
    city = models.CharField(max_length=100, blank=True, default="")
    postal_code = models.CharField(max_length=20, blank=True, default="")
    country = models.CharField(max_length=100, blank=True, default="")
    language = models.CharField(max_length=10, default="fr")
    timezone = models.CharField(max_length=50, default="UTC")
    avatar_url = models.URLField(blank=True, default="")

    class Meta:
        db_table = "iam_user_profiles"
