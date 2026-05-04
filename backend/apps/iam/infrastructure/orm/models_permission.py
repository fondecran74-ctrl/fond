"""Permission models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class PermissionCategory(AuditableModel):
    """Category grouping related permissions."""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "iam_permission_categories"
        verbose_name_plural = "Permission categories"

    def __str__(self) -> str:
        return self.name


class Permission(AuditableModel):
    """Fine-grained permission (resource:action format)."""

    class Action(models.TextChoices):
        CREATE = "create", "Create"
        READ = "read", "Read"
        UPDATE = "update", "Update"
        DELETE = "delete", "Delete"
        LIST = "list", "List"
        EXPORT = "export", "Export"
        IMPORT = "import", "Import"
        APPROVE = "approve", "Approve"
        REJECT = "reject", "Reject"
        ADMIN = "admin", "Administrate"

    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=20, choices=Action.choices)
    code = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, default="")
    category = models.ForeignKey(
        PermissionCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="permissions"
    )
    is_system = models.BooleanField(default=False)

    class Meta:
        db_table = "iam_permissions"
        ordering = ["resource", "action"]
        constraints = [
            models.UniqueConstraint(fields=["resource", "action"], name="unique_resource_action")
        ]

    def __str__(self) -> str:
        return f"{self.resource}:{self.action}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"{self.resource}:{self.action}"
        super().save(*args, **kwargs)
