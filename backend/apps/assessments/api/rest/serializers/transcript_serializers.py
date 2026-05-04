"""Transcript serializer."""
from rest_framework import serializers
from apps.assessments.infrastructure.orm.models import Transcript


class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
