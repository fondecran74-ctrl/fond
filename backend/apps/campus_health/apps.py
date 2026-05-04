"""App configuration for Campus Health."""
from django.apps import AppConfig

class CampusHealthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.campus_health"
    verbose_name = "Campus Health"
