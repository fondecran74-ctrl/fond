"""GradeAppeal serializer."""
from rest_framework import serializers
from apps.assessments.infrastructure.orm.models import GradeAppeal


class GradeAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeAppeal
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
