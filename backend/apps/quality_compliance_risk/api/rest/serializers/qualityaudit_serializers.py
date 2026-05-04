"""QualityAudit serializer."""
from rest_framework import serializers
from apps.quality_compliance_risk.infrastructure.orm.models import QualityAudit


class QualityAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityAudit
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
