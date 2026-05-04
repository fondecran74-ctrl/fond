"""Budget serializer."""
from rest_framework import serializers
from apps.finance.infrastructure.orm.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
