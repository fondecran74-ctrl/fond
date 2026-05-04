"""KPI serializer."""
from rest_framework import serializers
from apps.quality_compliance_risk.infrastructure.orm.models import KPI


class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
