"""IAM audit models."""
import uuid
from django.db import models
from apps.core.abstract_models import TimestampedModel


class AccessLog(TimestampedModel):
    """Log of access control decisions."""

    class Decision(models.TextChoices):
        ALLOWED = "ALLOWED", "Allowed"
        DENIED = "DENIED", "Denied"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, related_name="access_logs")
    resource = models.CharField(max_length=255)
    action = models.CharField(max_length=50)
    decision = models.CharField(max_length=10, choices=Decision.choices)
    decision_path = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default="")
    institution = models.ForeignKey(
        "org_structure.Institution", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        db_table = "iam_access_logs"
        indexes = [
            models.Index(fields=["user", "-created_at"]),
            models.Index(fields=["decision", "-created_at"]),
        ]


class AuditEntry(TimestampedModel):
    """Immutable audit trail entry."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    actor = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=100)
    resource_id = models.CharField(max_length=255)
    changes = models.JSONField(default=dict)
    metadata = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    correlation_id = models.CharField(max_length=255, blank=True, default="")

    class Meta:
        db_table = "iam_audit_entries"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["actor", "-created_at"]),
            models.Index(fields=["resource_type", "resource_id"]),
        ]
