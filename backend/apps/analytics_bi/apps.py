"""App configuration for Analytics & BI."""
from django.apps import AppConfig

class AnalyticsBiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.analytics_bi"
    verbose_name = "Analytics & BI"
