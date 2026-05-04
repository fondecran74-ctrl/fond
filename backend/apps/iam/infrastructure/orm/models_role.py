"""Role and permission assignment models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Role(AuditableModel):
    """Role definition with hierarchical levels."""

    class Level(models.IntegerChoices):
        SUPER_ADMIN = 0, "Super Administrateur (système)"
        GOVERNANCE = 1, "Gouvernance institutionnelle"
        ESTABLISHMENT_DIRECTION = 2, "Direction des établissements"
        FUNCTIONAL_DIRECTION = 3, "Direction fonctionnelle"
        OPERATIONAL_MANAGER = 4, "Responsables opérationnels"
        OPERATOR = 5, "Opérateurs/Techniciens"
        TEACHER = 6, "Enseignants"
        EXTERNAL_USER = 7, "Usagers externes"
        ACADEMIC_COORDINATION = 80, "Coordination académique transversale"
        ADVANCED_FUNCTIONAL = 90, "Administration fonctionnelle avancée"

    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, default="")
    level = models.IntegerField(choices=Level.choices)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    is_system = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    max_holders = models.PositiveIntegerField(null=True, blank=True)
    requires_approval = models.BooleanField(default=True)

    class Meta:
        db_table = "iam_roles"
        ordering = ["level", "name"]
        verbose_name = "Role"
        indexes = [
            models.Index(fields=["level"]),
            models.Index(fields=["code"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} (L{self.level})"


class UserRole(AuditableModel):
    """Assignment of a role to a user with scope."""
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="user_roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="user_roles")
    scope_institution = models.ForeignKey(
        "org_structure.Institution", on_delete=models.CASCADE, null=True, blank=True
    )
    scope_faculty = models.ForeignKey(
        "org_structure.Faculty", on_delete=models.CASCADE, null=True, blank=True
    )
    scope_department = models.ForeignKey(
        "org_structure.Department", on_delete=models.CASCADE, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    assigned_reason = models.TextField(blank=True, default="")
    approved_by = models.ForeignKey(
        "iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_roles"
    )

    class Meta:
        db_table = "iam_user_roles"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role", "scope_institution", "scope_faculty", "scope_department"],
                name="unique_user_role_scope",
            )
        ]

    def __str__(self) -> str:
        return f"{self.user} — {self.role}"


class RolePermission(AuditableModel):
    """Mapping of permissions to roles."""
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_permissions")
    permission = models.ForeignKey("iam.Permission", on_delete=models.CASCADE, related_name="role_permissions")

    class Meta:
        db_table = "iam_role_permissions"
        constraints = [
            models.UniqueConstraint(fields=["role", "permission"], name="unique_role_permission")
        ]
