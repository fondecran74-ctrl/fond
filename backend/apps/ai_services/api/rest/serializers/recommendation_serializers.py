"""Recommendation serializer."""
from rest_framework import serializers
from apps.ai_services.infrastructure.orm.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
