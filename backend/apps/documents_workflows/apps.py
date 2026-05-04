"""App configuration for Documents & Workflows."""
from django.apps import AppConfig

class DocumentsWorkflowsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.documents_workflows"
    verbose_name = "Documents & Workflows"
