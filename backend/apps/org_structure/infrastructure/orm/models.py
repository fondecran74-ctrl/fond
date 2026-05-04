"""Organizational structure models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Institution(AuditableModel):
    """Top-level institution (university group, consortium)."""
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=20, unique=True)
    legal_name = models.CharField(max_length=300, blank=True, default="")
    institution_type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True, default="")
    website = models.URLField(blank=True, default="")
    logo_url = models.URLField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    accreditation_number = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        db_table = "org_institutions"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Campus(AuditableModel):
    """Physical campus location."""
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="campuses")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "org_campuses"
        constraints = [models.UniqueConstraint(fields=["institution", "code"], name="unique_campus_code")]


class Faculty(AuditableModel):
    """Faculty or school within an institution."""
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="faculties")
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, blank=True, related_name="faculties")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    dean = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="dean_of")
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "org_faculties"
        verbose_name_plural = "Faculties"


class Department(AuditableModel):
    """Academic department within a faculty."""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    head = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="head_of")
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "org_departments"


class Laboratory(AuditableModel):
    """Research laboratory."""
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, related_name="laboratories")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="laboratories")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    director = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "org_laboratories"
        verbose_name_plural = "Laboratories"


class AdministrativeUnit(AuditableModel):
    """Administrative service unit."""
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="admin_units")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    unit_type = models.CharField(max_length=50)
    head = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "org_administrative_units"
