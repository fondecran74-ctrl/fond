"""App configuration for Academic Catalog."""
from django.apps import AppConfig

class AcademicCatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.academic_catalog"
    verbose_name = "Academic Catalog"
