"""International relations models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class PartnerInstitution(AuditableModel):
    """Partner institution for international exchanges."""
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField(blank=True, default="")
    agreement_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "intl_partners"


class ExchangeAgreement(InstitutionScopedModel):
    """Exchange agreement with a partner."""
    partner = models.ForeignKey(PartnerInstitution, on_delete=models.CASCADE, related_name="agreements")
    title = models.CharField(max_length=300)
    signed_at = models.DateField()
    expires_at = models.DateField()
    max_students_outgoing = models.PositiveIntegerField(default=5)
    max_students_incoming = models.PositiveIntegerField(default=5)
    status = models.CharField(max_length=20, default="ACTIVE")

    class Meta:
        db_table = "intl_agreements"


class MobilityApplication(AuditableModel):
    """Student mobility application."""
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="mobility_applications")
    agreement = models.ForeignKey(ExchangeAgreement, on_delete=models.CASCADE, related_name="applications")
    direction = models.CharField(max_length=10, choices=[("OUTGOING", "Outgoing"), ("INCOMING", "Incoming")])
    semester = models.ForeignKey("academic_catalog.Semester", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="SUBMITTED")
    motivation = models.TextField()

    class Meta:
        db_table = "intl_mobility_applications"
