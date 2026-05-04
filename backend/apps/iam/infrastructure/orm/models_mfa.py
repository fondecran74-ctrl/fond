"""MFA settings models."""
import uuid
from django.db import models
from apps.core.abstract_models import TimestampedModel


class MFASetting(TimestampedModel):
    """Multi-Factor Authentication settings per user."""

    class MFAType(models.TextChoices):
        TOTP = "TOTP", "Time-based OTP"
        WEBAUTHN = "WEBAUTHN", "WebAuthn/FIDO2"
        SMS = "SMS", "SMS"
        EMAIL = "EMAIL", "Email"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="mfa_settings")
    mfa_type = models.CharField(max_length=20, choices=MFAType.choices)
    is_enabled = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)
    secret_encrypted = models.TextField(blank=True, default="")
    recovery_codes_encrypted = models.TextField(blank=True, default="")
    verified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "iam_mfa_settings"
        constraints = [
            models.UniqueConstraint(fields=["user", "mfa_type"], name="unique_user_mfa_type")
        ]
