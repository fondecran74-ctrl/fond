"""Library models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class CatalogItem(AuditableModel):
    """Library catalog item."""
    title = models.CharField(max_length=500)
    isbn = models.CharField(max_length=20, blank=True, default="")
    authors = models.TextField()
    publisher = models.CharField(max_length=200, blank=True, default="")
    publication_year = models.PositiveIntegerField(null=True, blank=True)
    item_type = models.CharField(max_length=30)
    copies_total = models.PositiveIntegerField(default=1)
    copies_available = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=100, blank=True, default="")
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="catalog_items")

    class Meta:
        db_table = "lib_catalog"


class Loan(AuditableModel):
    """Book loan."""
    item = models.ForeignKey(CatalogItem, on_delete=models.CASCADE, related_name="loans")
    borrower = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="library_loans")
    borrowed_at = models.DateTimeField()
    due_at = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="ACTIVE")

    class Meta:
        db_table = "lib_loans"


class Reservation(AuditableModel):
    """Item reservation."""
    item = models.ForeignKey(CatalogItem, on_delete=models.CASCADE, related_name="reservations")
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="library_reservations")
    reserved_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    status = models.CharField(max_length=20, default="ACTIVE")

    class Meta:
        db_table = "lib_reservations"
