"""App configuration for Quality, Compliance & Risk."""
from django.apps import AppConfig

class QualityComplianceRiskConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.quality_compliance_risk"
    verbose_name = "Quality, Compliance & Risk"
