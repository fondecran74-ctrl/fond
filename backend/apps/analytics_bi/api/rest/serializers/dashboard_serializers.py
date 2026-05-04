"""Dashboard serializer."""
from rest_framework import serializers
from apps.analytics_bi.infrastructure.orm.models import Dashboard


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
