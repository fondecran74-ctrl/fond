"""User-specific filters."""
import django_filters
from apps.iam.infrastructure.orm.models_user import User


class UserSearchFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = User
        fields = ["search"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            models__icontains=value
        ) | queryset.filter(
            email__icontains=value
        ) | queryset.filter(
            first_name__icontains=value
        ) | queryset.filter(
            last_name__icontains=value
        )
