"""Grade serializer."""
from rest_framework import serializers
from apps.assessments.infrastructure.orm.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
