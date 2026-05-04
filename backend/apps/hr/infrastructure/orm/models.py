"""HR models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Employee(AuditableModel):
    """Employee profile linked to a user account."""
    user = models.OneToOneField("iam.User", on_delete=models.CASCADE, related_name="employee_profile")
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey("org_structure.Department", on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=200)
    hire_date = models.DateField()
    contract_type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="employees")

    class Meta:
        db_table = "hr_employees"


class Contract(AuditableModel):
    """Employment contract."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="contracts")
    contract_type = models.CharField(max_length=30)
    starts_at = models.DateField()
    ends_at = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="EUR")
    status = models.CharField(max_length=20, default="ACTIVE")

    class Meta:
        db_table = "hr_contracts"


class LeaveRequest(AuditableModel):
    """Employee leave request."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="leave_requests")
    leave_type = models.CharField(max_length=30)
    starts_at = models.DateField()
    ends_at = models.DateField()
    days = models.DecimalField(max_digits=5, decimal_places=1)
    status = models.CharField(max_length=20, default="PENDING")
    approved_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.TextField(blank=True, default="")

    class Meta:
        db_table = "hr_leave_requests"


class PerformanceEvaluation(AuditableModel):
    """Employee performance evaluation."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="evaluations")
    evaluator = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="evaluations_given")
    period = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    comments = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20, default="DRAFT")

    class Meta:
        db_table = "hr_evaluations"
