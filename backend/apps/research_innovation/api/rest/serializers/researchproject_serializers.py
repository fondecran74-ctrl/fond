"""ResearchProject serializer."""
from rest_framework import serializers
from apps.research_innovation.infrastructure.orm.models import ResearchProject


class ResearchProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchProject
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
