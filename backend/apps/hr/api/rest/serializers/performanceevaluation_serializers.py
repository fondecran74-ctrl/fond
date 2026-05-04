"""PerformanceEvaluation serializer."""
from rest_framework import serializers
from apps.hr.infrastructure.orm.models import PerformanceEvaluation


class PerformanceEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceEvaluation
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
