"""MobilityApplication serializer."""
from rest_framework import serializers
from apps.international_relations.infrastructure.orm.models import MobilityApplication


class MobilityApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilityApplication
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
