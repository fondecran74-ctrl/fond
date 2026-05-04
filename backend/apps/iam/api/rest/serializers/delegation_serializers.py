"""DelegationSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_delegation import Delegation


class DelegationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegation
        fields = ["id", "delegator", "delegate", "delegation_type", "status", "reason", "starts_at", "ends_at"]
        read_only_fields = ["id", "created_at"]
