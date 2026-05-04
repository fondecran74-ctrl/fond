"""Delegation models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Delegation(AuditableModel):
    """Temporary delegation of access rights."""

    class DelegationType(models.TextChoices):
        FULL = "FULL", "Full delegation"
        PARTIAL = "PARTIAL", "Partial delegation"
        SIGNATURE = "SIGNATURE", "Signature delegation"
        INTERIM = "INTERIM", "Interim/Acting"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending approval"
        ACTIVE = "ACTIVE", "Active"
        EXPIRED = "EXPIRED", "Expired"
        REVOKED = "REVOKED", "Revoked"

    delegator = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="delegations_given")
    delegate = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="delegations_received")
    delegation_type = models.CharField(max_length=20, choices=DelegationType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    reason = models.TextField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    approved_by = models.ForeignKey(
        "iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="delegation_approvals"
    )
    roles = models.ManyToManyField("iam.Role", blank=True, related_name="delegations")
    permissions = models.ManyToManyField("iam.Permission", blank=True, related_name="delegations")

    class Meta:
        db_table = "iam_delegations"
        ordering = ["-starts_at"]

    def __str__(self) -> str:
        return f"Delegation {self.delegator} → {self.delegate} ({self.status})"
