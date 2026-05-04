"""Accreditation serializer."""
from rest_framework import serializers
from apps.quality_compliance_risk.infrastructure.orm.models import Accreditation


class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
