"""Ranking serializer."""
from rest_framework import serializers
from apps.admissions.infrastructure.orm.models import Ranking


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
