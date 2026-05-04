"""AcademicRecord serializer."""
from rest_framework import serializers
from apps.student_lifecycle.infrastructure.orm.models import AcademicRecord


class AcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicRecord
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
