"""Admissions models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Campaign(InstitutionScopedModel):
    """Admission campaign."""
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        OPEN = "OPEN", "Open"
        CLOSED = "CLOSED", "Closed"
        COMPLETED = "COMPLETED", "Completed"

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    academic_year = models.ForeignKey("academic_catalog.AcademicYear", on_delete=models.CASCADE)
    program = models.ForeignKey("academic_catalog.Program", on_delete=models.CASCADE, related_name="campaigns")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    opens_at = models.DateTimeField()
    closes_at = models.DateTimeField()
    max_places = models.PositiveIntegerField()
    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "adm_campaigns"


class Candidate(AuditableModel):
    """Candidate — created ONLY by institution agents, never self-registered."""
    user = models.OneToOneField("iam.User", on_delete=models.CASCADE, related_name="candidate_profile")
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="candidates")
    status = models.CharField(max_length=30, default="SUBMITTED")
    submitted_at = models.DateTimeField(null=True, blank=True)
    total_score = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    decision = models.CharField(max_length=20, blank=True, default="")
    decision_date = models.DateField(null=True, blank=True)
    decision_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="admission_decisions")

    class Meta:
        db_table = "adm_candidates"


class Application(AuditableModel):
    """Application submitted for a candidate."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="applications")
    program = models.ForeignKey("academic_catalog.Program", on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default="DRAFT")
    motivation_letter = models.TextField(blank=True, default="")
    notes = models.TextField(blank=True, default="")

    class Meta:
        db_table = "adm_applications"


class AdmissionDocument(AuditableModel):
    """Document submitted as part of an application."""
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(max_length=50)
    file_url = models.URLField()
    original_filename = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "adm_documents"


class AdmissionCommittee(InstitutionScopedModel):
    """Committee evaluating admission applications."""
    name = models.CharField(max_length=200)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="committees")
    chairperson = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "adm_committees"


class Interview(AuditableModel):
    """Interview scheduled for a candidate."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="interviews")
    committee = models.ForeignKey(AdmissionCommittee, on_delete=models.CASCADE, related_name="interviews")
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    location = models.CharField(max_length=200, blank=True, default="")
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, default="")

    class Meta:
        db_table = "adm_interviews"


class Ranking(AuditableModel):
    """Final ranking of candidates."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="rankings")
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="ranking_entries")
    rank = models.PositiveIntegerField()
    total_score = models.DecimalField(max_digits=8, decimal_places=2)
    decision = models.CharField(max_length=20)

    class Meta:
        db_table = "adm_rankings"
        constraints = [models.UniqueConstraint(fields=["campaign", "candidate"], name="unique_campaign_candidate_rank")]
