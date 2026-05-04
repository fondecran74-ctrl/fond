"""Candidate serializer."""
from rest_framework import serializers
from apps.admissions.infrastructure.orm.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
