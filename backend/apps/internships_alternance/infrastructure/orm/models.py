"""Internship and alternance models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class InternshipOffer(AuditableModel):
    """Internship or alternance offer from a company."""
    company_name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=200)
    duration_months = models.PositiveIntegerField()
    is_alternance = models.BooleanField(default=False)
    compensation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    starts_at = models.DateField()
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    contact_email = models.EmailField()

    class Meta:
        db_table = "intern_offers"


class InternshipConvention(AuditableModel):
    """Internship agreement/convention."""
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="internship_conventions")
    offer = models.ForeignKey(InternshipOffer, on_delete=models.CASCADE, related_name="conventions")
    academic_supervisor = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="supervised_internships")
    company_supervisor_name = models.CharField(max_length=200)
    company_supervisor_email = models.EmailField()
    starts_at = models.DateField()
    ends_at = models.DateField()
    status = models.CharField(max_length=20, default="DRAFT")
    signed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "intern_conventions"


class InternshipEvaluation(AuditableModel):
    """Evaluation of an internship."""
    convention = models.ForeignKey(InternshipConvention, on_delete=models.CASCADE, related_name="evaluations")
    evaluator = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    comments = models.TextField(blank=True, default="")
    evaluated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "intern_evaluations"
