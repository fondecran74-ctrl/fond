"""Finance models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Budget(InstitutionScopedModel):
    """Budget definition."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    fiscal_year = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2)
    consumed_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    department = models.ForeignKey("org_structure.Department", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default="DRAFT")
    approved_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "fin_budgets"


class Invoice(AuditableModel):
    """Invoice (tuition, fees, services)."""
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        ISSUED = "ISSUED", "Issued"
        PAID = "PAID", "Paid"
        OVERDUE = "OVERDUE", "Overdue"
        CANCELLED = "CANCELLED", "Cancelled"

    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, null=True, blank=True, related_name="invoices")
    invoice_number = models.CharField(max_length=30, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="EUR")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    issued_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateField()
    paid_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="invoices")

    class Meta:
        db_table = "fin_invoices"


class Payment(AuditableModel):
    """Payment record."""
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    transaction_id = models.CharField(max_length=100, blank=True, default="")
    paid_at = models.DateTimeField()
    status = models.CharField(max_length=20, default="COMPLETED")

    class Meta:
        db_table = "fin_payments"


class Scholarship(AuditableModel):
    """Scholarship definition."""
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="EUR")
    criteria = models.TextField()
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="scholarships")
    academic_year = models.ForeignKey("academic_catalog.AcademicYear", on_delete=models.CASCADE)
    max_recipients = models.PositiveIntegerField()

    class Meta:
        db_table = "fin_scholarships"


class ScholarshipAward(AuditableModel):
    """Scholarship awarded to a student."""
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name="awards")
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="scholarship_awards")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="ACTIVE")
    awarded_at = models.DateField()

    class Meta:
        db_table = "fin_scholarship_awards"
