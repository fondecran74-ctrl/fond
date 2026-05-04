"""Examination serializer."""
from rest_framework import serializers
from apps.assessments.infrastructure.orm.models import Examination


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
