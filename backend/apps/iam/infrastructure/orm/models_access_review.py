"""Access review models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class AccessReview(AuditableModel):
    """Periodic access review campaign."""

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    reviewer = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="access_reviews")
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    institution = models.ForeignKey(
        "org_structure.Institution", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "iam_access_reviews"


class AccessReviewItem(AuditableModel):
    """Individual item within an access review."""

    class Decision(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REVOKED = "REVOKED", "Revoked"
        MODIFIED = "MODIFIED", "Modified"

    review = models.ForeignKey(AccessReview, on_delete=models.CASCADE, related_name="items")
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    role = models.ForeignKey("iam.Role", on_delete=models.CASCADE)
    decision = models.CharField(max_length=20, choices=Decision.choices, default=Decision.PENDING)
    justification = models.TextField(blank=True, default="")

    class Meta:
        db_table = "iam_access_review_items"
