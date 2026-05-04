"""PolicyDecision serializer."""
from rest_framework import serializers
from apps.audit_traceability.infrastructure.orm.models import PolicyDecision


class PolicyDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyDecision
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
