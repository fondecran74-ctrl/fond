"""Audit and traceability models."""
import uuid
from django.db import models
from apps.core.abstract_models import TimestampedModel


class AuditLog(TimestampedModel):
    """Immutable audit log entry."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    actor_id = models.UUIDField(null=True, blank=True)
    actor_email = models.EmailField(blank=True, default="")
    action = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=100)
    resource_id = models.CharField(max_length=255)
    old_values = models.JSONField(default=dict)
    new_values = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default="")
    correlation_id = models.CharField(max_length=255, blank=True, default="")
    institution_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "audit_logs"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["actor_id", "-created_at"]),
            models.Index(fields=["resource_type", "resource_id"]),
            models.Index(fields=["action", "-created_at"]),
            models.Index(fields=["institution_id", "-created_at"]),
        ]


class PolicyDecision(TimestampedModel):
    """Record of authorization policy decisions."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_id = models.UUIDField()
    resource = models.CharField(max_length=255)
    action = models.CharField(max_length=50)
    decision = models.CharField(max_length=10)
    policy_type = models.CharField(max_length=20)
    decision_path = models.JSONField(default=list)
    evaluation_time_ms = models.FloatField(default=0)

    class Meta:
        db_table = "audit_policy_decisions"
        indexes = [
            models.Index(fields=["subject_id", "-created_at"]),
            models.Index(fields=["decision", "-created_at"]),
        ]


class ComplianceEvidence(TimestampedModel):
    """Compliance evidence record."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    framework = models.CharField(max_length=50)
    control_id = models.CharField(max_length=50)
    description = models.TextField()
    evidence_url = models.URLField(blank=True, default="")
    status = models.CharField(max_length=20, default="COLLECTED")
    collected_at = models.DateTimeField()
    collector = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "audit_compliance_evidence"
