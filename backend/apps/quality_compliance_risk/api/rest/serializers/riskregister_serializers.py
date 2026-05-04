"""RiskRegister serializer."""
from rest_framework import serializers
from apps.quality_compliance_risk.infrastructure.orm.models import RiskRegister


class RiskRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskRegister
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
