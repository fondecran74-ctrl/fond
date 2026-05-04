"""App configuration for Student Lifecycle."""
from django.apps import AppConfig

class StudentLifecycleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.student_lifecycle"
    verbose_name = "Student Lifecycle"
