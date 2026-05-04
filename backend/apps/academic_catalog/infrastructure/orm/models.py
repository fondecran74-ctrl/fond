"""Academic catalog models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Program(InstitutionScopedModel):
    """Academic program (Licence, Master, Doctorat, etc.)."""
    class Level(models.TextChoices):
        LICENCE = "LICENCE", "Licence"
        MASTER = "MASTER", "Master"
        DOCTORATE = "DOCTORATE", "Doctorat"
        DUT = "DUT", "DUT"
        BTS = "BTS", "BTS"
        ENGINEERING = "ENGINEERING", "Ingénieur"
        MBA = "MBA", "MBA"

    name = models.CharField(max_length=300)
    code = models.CharField(max_length=20, unique=True)
    level = models.CharField(max_length=20, choices=Level.choices)
    faculty = models.ForeignKey("org_structure.Faculty", on_delete=models.CASCADE, related_name="programs")
    department = models.ForeignKey("org_structure.Department", on_delete=models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, default="")
    total_credits = models.PositiveIntegerField(default=180)
    duration_semesters = models.PositiveIntegerField(default=6)
    is_active = models.BooleanField(default=True)
    accreditation_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "acad_programs"
        ordering = ["name"]


class Course(AuditableModel):
    """Individual course/module."""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField(default=3)
    hours_lecture = models.PositiveIntegerField(default=0)
    hours_td = models.PositiveIntegerField(default=0)
    hours_tp = models.PositiveIntegerField(default=0)
    semester = models.PositiveIntegerField()
    description = models.TextField(blank=True, default="")
    is_mandatory = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    coordinator = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "acad_courses"
        ordering = ["program", "semester", "code"]


class AcademicYear(AuditableModel):
    """Academic year definition."""
    name = models.CharField(max_length=20, unique=True)
    starts_at = models.DateField()
    ends_at = models.DateField()
    is_current = models.BooleanField(default=False)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="academic_years")

    class Meta:
        db_table = "acad_academic_years"


class Semester(AuditableModel):
    """Semester within an academic year."""
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name="semesters")
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    starts_at = models.DateField()
    ends_at = models.DateField()

    class Meta:
        db_table = "acad_semesters"


class Prerequisite(AuditableModel):
    """Course prerequisites."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prerequisites")
    required_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prerequisite_for")
    is_mandatory = models.BooleanField(default=True)
    minimum_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "acad_prerequisites"
        constraints = [models.UniqueConstraint(fields=["course", "required_course"], name="unique_prerequisite")]


class LearningOutcome(AuditableModel):
    """Learning outcome for a course or program."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name="learning_outcomes")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True, related_name="learning_outcomes")
    code = models.CharField(max_length=20)
    description = models.TextField()
    level = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        db_table = "acad_learning_outcomes"
