"""Break-glass request models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class BreakGlassRequest(AuditableModel):
    """Emergency elevated access request."""

    class Status(models.TextChoices):
        REQUESTED = "REQUESTED", "Requested"
        APPROVED = "APPROVED", "Approved"
        ACTIVE = "ACTIVE", "Active"
        EXPIRED = "EXPIRED", "Expired"
        REVOKED = "REVOKED", "Revoked"
        DENIED = "DENIED", "Denied"

    requester = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="break_glass_requests")
    approver = models.ForeignKey(
        "iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="break_glass_approvals"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REQUESTED)
    justification = models.TextField()
    elevated_roles = models.ManyToManyField("iam.Role", related_name="break_glass_requests")
    starts_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)
    actions_taken = models.TextField(blank=True, default="")

    class Meta:
        db_table = "iam_break_glass_requests"
        ordering = ["-created_at"]
