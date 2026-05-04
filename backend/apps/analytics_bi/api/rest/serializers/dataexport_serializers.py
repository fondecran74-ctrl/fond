"""DataExport serializer."""
from rest_framework import serializers
from apps.analytics_bi.infrastructure.orm.models import DataExport


class DataExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataExport
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
