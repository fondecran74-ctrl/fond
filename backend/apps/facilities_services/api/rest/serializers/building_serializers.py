"""Building serializer."""
from rest_framework import serializers
from apps.facilities_services.infrastructure.orm.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
