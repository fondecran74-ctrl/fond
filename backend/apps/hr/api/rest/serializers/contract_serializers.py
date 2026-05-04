"""Contract serializer."""
from rest_framework import serializers
from apps.hr.infrastructure.orm.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
