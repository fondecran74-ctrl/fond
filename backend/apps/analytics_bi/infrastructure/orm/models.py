"""Analytics and BI models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Dashboard(AuditableModel):
    """Custom dashboard definition."""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="dashboards")
    layout = models.JSONField(default=dict)
    is_shared = models.BooleanField(default=False)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "analytics_dashboards"


class Report(AuditableModel):
    """Saved report."""
    name = models.CharField(max_length=200)
    report_type = models.CharField(max_length=50)
    query = models.JSONField()
    parameters = models.JSONField(default=dict)
    owner = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="reports")
    schedule = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        db_table = "analytics_reports"


class DataExport(AuditableModel):
    """Data export request."""
    name = models.CharField(max_length=200)
    format = models.CharField(max_length=10)
    status = models.CharField(max_length=20, default="PENDING")
    file_url = models.URLField(blank=True, default="")
    requested_by = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "analytics_exports"
