"""App configuration for Audit & Traceability."""
from django.apps import AppConfig

class AuditTraceabilityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.audit_traceability"
    verbose_name = "Audit & Traceability"
