"""ComplianceEvidence serializer."""
from rest_framework import serializers
from apps.audit_traceability.infrastructure.orm.models import ComplianceEvidence


class ComplianceEvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceEvidence
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
