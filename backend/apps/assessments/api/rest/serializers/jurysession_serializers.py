"""JurySession serializer."""
from rest_framework import serializers
from apps.assessments.infrastructure.orm.models import JurySession


class JurySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JurySession
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
