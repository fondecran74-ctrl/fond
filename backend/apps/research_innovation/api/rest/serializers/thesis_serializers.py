"""Thesis serializer."""
from rest_framework import serializers
from apps.research_innovation.infrastructure.orm.models import Thesis


class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
