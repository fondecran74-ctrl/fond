"""IAM filters."""
import django_filters
from apps.iam.infrastructure.orm.models_user import User


class UserFilter(django_filters.FilterSet):
    user_type = django_filters.ChoiceFilter(choices=User.UserType.choices)
    account_status = django_filters.ChoiceFilter(choices=User.AccountStatus.choices)
    institution = django_filters.UUIDFilter()

    class Meta:
        model = User
        fields = ["user_type", "account_status", "institution"]
