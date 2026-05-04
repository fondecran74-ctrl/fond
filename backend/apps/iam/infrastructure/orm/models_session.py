"""Session models."""
import uuid
from django.db import models
from apps.core.abstract_models import TimestampedModel


class UserSession(TimestampedModel):
    """User session tracking."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="sessions")
    session_key = models.CharField(max_length=255, unique=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, default="")
    device_type = models.CharField(max_length=50, blank=True, default="")
    is_active = models.BooleanField(default=True)
    last_activity = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField()
    active_role = models.ForeignKey(
        "iam.Role", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        db_table = "iam_sessions"
        indexes = [
            models.Index(fields=["user", "is_active"]),
            models.Index(fields=["expires_at"]),
        ]
