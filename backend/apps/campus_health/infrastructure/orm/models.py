"""Campus health models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class MedicalRecord(AuditableModel):
    """Student medical record (encrypted/classified)."""
    student = models.OneToOneField("iam.User", on_delete=models.CASCADE, related_name="medical_record")
    blood_type = models.CharField(max_length=5, blank=True, default="")
    allergies = models.TextField(blank=True, default="")
    chronic_conditions = models.TextField(blank=True, default="")
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = models.CharField(max_length=20)
    insurance_provider = models.CharField(max_length=200, blank=True, default="")
    insurance_number = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        db_table = "health_medical_records"


class Appointment(AuditableModel):
    """Medical appointment."""
    patient = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="health_appointments")
    practitioner = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="medical_appointments")
    appointment_type = models.CharField(max_length=30)
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    status = models.CharField(max_length=20, default="SCHEDULED")
    notes = models.TextField(blank=True, default="")

    class Meta:
        db_table = "health_appointments"
