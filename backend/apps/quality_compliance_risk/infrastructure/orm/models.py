"""Quality, compliance and risk models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Accreditation(InstitutionScopedModel):
    """Accreditation record."""
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="ACTIVE")
    granted_at = models.DateField()
    expires_at = models.DateField()
    scope = models.TextField()

    class Meta:
        db_table = "qcr_accreditations"


class QualityAudit(InstitutionScopedModel):
    """Quality audit."""
    title = models.CharField(max_length=200)
    audit_type = models.CharField(max_length=50)
    scheduled_at = models.DateField()
    completed_at = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default="PLANNED")
    findings = models.TextField(blank=True, default="")
    auditor = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "qcr_audits"


class RiskRegister(InstitutionScopedModel):
    """Risk register entry."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    likelihood = models.PositiveIntegerField()
    impact = models.PositiveIntegerField()
    risk_score = models.PositiveIntegerField()
    mitigation = models.TextField(blank=True, default="")
    owner = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default="OPEN")

    class Meta:
        db_table = "qcr_risks"


class KPI(InstitutionScopedModel):
    """Key Performance Indicator."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, default="")
    target_value = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=20)
    period = models.CharField(max_length=20)

    class Meta:
        db_table = "qcr_kpis"
