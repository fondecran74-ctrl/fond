"""Graduation serializer."""
from rest_framework import serializers
from apps.student_lifecycle.infrastructure.orm.models import Graduation


class GraduationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduation
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
