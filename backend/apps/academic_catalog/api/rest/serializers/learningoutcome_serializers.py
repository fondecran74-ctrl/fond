"""LearningOutcome serializer."""
from rest_framework import serializers
from apps.academic_catalog.infrastructure.orm.models import LearningOutcome


class LearningOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningOutcome
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
