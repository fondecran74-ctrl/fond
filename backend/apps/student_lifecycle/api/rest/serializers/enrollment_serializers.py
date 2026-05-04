"""Enrollment serializer."""
from rest_framework import serializers
from apps.student_lifecycle.infrastructure.orm.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
