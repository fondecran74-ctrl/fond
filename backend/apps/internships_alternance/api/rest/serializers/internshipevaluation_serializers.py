"""InternshipEvaluation serializer."""
from rest_framework import serializers
from apps.internships_alternance.infrastructure.orm.models import InternshipEvaluation


class InternshipEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipEvaluation
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
