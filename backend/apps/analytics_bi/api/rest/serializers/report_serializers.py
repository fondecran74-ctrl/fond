"""Report serializer."""
from rest_framework import serializers
from apps.analytics_bi.infrastructure.orm.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
