"""ITSM and cybersecurity models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Ticket(AuditableModel):
    """IT support ticket."""
    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        CRITICAL = "CRITICAL", "Critical"

    title = models.CharField(max_length=300)
    description = models.TextField()
    reporter = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="reported_tickets")
    assignee = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tickets")
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField(max_length=20, default="OPEN")
    category = models.CharField(max_length=50)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="tickets")

    class Meta:
        db_table = "itsm_tickets"


class Incident(AuditableModel):
    """Security incident."""
    title = models.CharField(max_length=300)
    description = models.TextField()
    severity = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="OPEN")
    detected_at = models.DateTimeField()
    resolved_at = models.DateTimeField(null=True, blank=True)
    reporter = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="incidents")

    class Meta:
        db_table = "itsm_incidents"


class ITAsset(AuditableModel):
    """IT asset inventory."""
    name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, unique=True)
    assigned_to = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True, default="")
    status = models.CharField(max_length=20, default="ACTIVE")
    purchase_date = models.DateField(null=True, blank=True)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="it_assets")

    class Meta:
        db_table = "itsm_assets"
