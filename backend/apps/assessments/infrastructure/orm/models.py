"""Assessment and grading models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Examination(AuditableModel):
    """Examination definition."""
    class ExamType(models.TextChoices):
        MIDTERM = "MIDTERM", "Midterm"
        FINAL = "FINAL", "Final"
        CONTINUOUS = "CONTINUOUS", "Continuous assessment"
        ORAL = "ORAL", "Oral exam"
        PRACTICAL = "PRACTICAL", "Practical exam"
        PROJECT = "PROJECT", "Project"

    course = models.ForeignKey("academic_catalog.Course", on_delete=models.CASCADE, related_name="examinations")
    semester = models.ForeignKey("academic_catalog.Semester", on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=20, choices=ExamType.choices)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    max_score = models.DecimalField(max_digits=6, decimal_places=2, default=20)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    location = models.CharField(max_length=200, blank=True, default="")
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = "assess_examinations"


class Grade(AuditableModel):
    """Individual student grade."""
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="grades")
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name="grades")
    score = models.DecimalField(max_digits=6, decimal_places=2)
    letter_grade = models.CharField(max_length=5, blank=True, default="")
    graded_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="graded_exams")
    graded_at = models.DateTimeField(null=True, blank=True)
    is_locked = models.BooleanField(default=False)
    locked_at = models.DateTimeField(null=True, blank=True)
    locked_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="locked_grades")
    comment = models.TextField(blank=True, default="")

    class Meta:
        db_table = "assess_grades"
        constraints = [models.UniqueConstraint(fields=["student", "examination"], name="unique_student_exam_grade")]


class GradeAppeal(AuditableModel):
    """Grade appeal by student."""
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="appeals")
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, default="SUBMITTED")
    decision = models.TextField(blank=True, default="")
    decided_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="appeal_decisions")

    class Meta:
        db_table = "assess_grade_appeals"


class JurySession(AuditableModel):
    """Jury deliberation session."""
    name = models.CharField(max_length=200)
    semester = models.ForeignKey("academic_catalog.Semester", on_delete=models.CASCADE)
    program = models.ForeignKey("academic_catalog.Program", on_delete=models.CASCADE)
    date = models.DateTimeField()
    chairperson = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)
    is_finalized = models.BooleanField(default=False)
    minutes = models.TextField(blank=True, default="")

    class Meta:
        db_table = "assess_jury_sessions"


class Transcript(AuditableModel):
    """Official transcript document."""
    student = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="transcripts")
    generated_at = models.DateTimeField(auto_now_add=True)
    document_url = models.URLField(blank=True, default="")
    is_official = models.BooleanField(default=False)
    verified_by = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "assess_transcripts"
