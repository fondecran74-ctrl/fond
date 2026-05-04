"""AcademicYear serializer."""
from rest_framework import serializers
from apps.academic_catalog.infrastructure.orm.models import AcademicYear


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
