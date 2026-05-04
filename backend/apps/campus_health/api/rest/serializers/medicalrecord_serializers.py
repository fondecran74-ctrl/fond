"""MedicalRecord serializer."""
from rest_framework import serializers
from apps.campus_health.infrastructure.orm.models import MedicalRecord


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
