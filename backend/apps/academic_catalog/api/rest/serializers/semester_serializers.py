"""Semester serializer."""
from rest_framework import serializers
from apps.academic_catalog.infrastructure.orm.models import Semester


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
