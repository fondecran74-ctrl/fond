"""Student lifecycle models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Enrollment(AuditableModel):
    """Student enrollment in a program."""
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        SUSPENDED = "SUSPENDED", "Suspended"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"
        GRADUATED = "GRADUATED", "Graduated"
        EXPELLED = "EXPELLED", "Expelled"
        ON_LEAVE = "ON_LEAVE", "On leave"

    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="enrollments")
    program = models.ForeignKey("academic_catalog.Program", on_delete=models.CASCADE, related_name="enrollments")
    academic_year = models.ForeignKey("academic_catalog.AcademicYear", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    student_id_number = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "sl_enrollments"


class Registration(AuditableModel):
    """Course registration for a semester."""
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="registrations")
    course = models.ForeignKey("academic_catalog.Course", on_delete=models.CASCADE)
    semester = models.ForeignKey("academic_catalog.Semester", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="REGISTERED")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sl_registrations"
        constraints = [models.UniqueConstraint(fields=["enrollment", "course", "semester"], name="unique_registration")]


class AcademicRecord(AuditableModel):
    """Academic record for a student."""
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="academic_records")
    semester = models.ForeignKey("academic_catalog.Semester", on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    credits_earned = models.PositiveIntegerField(default=0)
    credits_attempted = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "sl_academic_records"


class Graduation(AuditableModel):
    """Graduation record."""
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="graduations")
    graduation_date = models.DateField()
    diploma_number = models.CharField(max_length=50, unique=True)
    honors = models.CharField(max_length=50, blank=True, default="")
    final_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    total_credits = models.PositiveIntegerField()

    class Meta:
        db_table = "sl_graduations"


class Transfer(AuditableModel):
    """Student transfer between programs."""
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="transfers")
    from_program = models.ForeignKey("academic_catalog.Program", on_delete=models.CASCADE, related_name="transfers_out")
    to_program = models.ForeignKey("academic_catalog.Program", on_delete=models.CASCADE, related_name="transfers_in")
    status = models.CharField(max_length=20, default="PENDING")
    reason = models.TextField()
    approved_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_transfers")

    class Meta:
        db_table = "sl_transfers"


class LeaveOfAbsence(AuditableModel):
    """Leave of absence request."""
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="leaves")
    reason = models.TextField()
    starts_at = models.DateField()
    ends_at = models.DateField()
    status = models.CharField(max_length=20, default="PENDING")
    approved_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "sl_leaves"
