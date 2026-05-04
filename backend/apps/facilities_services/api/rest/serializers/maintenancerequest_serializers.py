"""MaintenanceRequest serializer."""
from rest_framework import serializers
from apps.facilities_services.infrastructure.orm.models import MaintenanceRequest


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
