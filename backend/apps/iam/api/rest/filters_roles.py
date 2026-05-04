"""Role-specific filters."""
import django_filters
from apps.iam.infrastructure.orm.models_role import Role


class RoleFilter(django_filters.FilterSet):
    level = django_filters.NumberFilter()
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Role
        fields = ["level", "is_active"]
