"""Research and innovation models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class ResearchProject(InstitutionScopedModel):
    """Research project."""
    title = models.CharField(max_length=500)
    code = models.CharField(max_length=20, unique=True)
    principal_investigator = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="research_projects_pi")
    laboratory = models.ForeignKey("org_structure.Laboratory", on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    starts_at = models.DateField()
    ends_at = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default="ACTIVE")
    funding_source = models.CharField(max_length=200, blank=True, default="")

    class Meta:
        db_table = "res_projects"


class Publication(AuditableModel):
    """Research publication."""
    project = models.ForeignKey(ResearchProject, on_delete=models.SET_NULL, null=True, blank=True, related_name="publications")
    title = models.CharField(max_length=500)
    journal = models.CharField(max_length=300, blank=True, default="")
    doi = models.CharField(max_length=100, blank=True, default="")
    published_at = models.DateField(null=True, blank=True)
    publication_type = models.CharField(max_length=50)

    class Meta:
        db_table = "res_publications"


class Grant(AuditableModel):
    """Research grant."""
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE, related_name="grants")
    title = models.CharField(max_length=300)
    funding_body = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="EUR")
    starts_at = models.DateField()
    ends_at = models.DateField()
    status = models.CharField(max_length=20, default="ACTIVE")

    class Meta:
        db_table = "res_grants"


class Thesis(AuditableModel):
    """PhD thesis."""
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="theses")
    supervisor = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="supervised_theses")
    title = models.CharField(max_length=500)
    laboratory = models.ForeignKey("org_structure.Laboratory", on_delete=models.SET_NULL, null=True, blank=True)
    started_at = models.DateField()
    defended_at = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default="IN_PROGRESS")

    class Meta:
        db_table = "res_theses"
