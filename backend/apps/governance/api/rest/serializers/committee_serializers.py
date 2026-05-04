"""Committee serializer."""
from rest_framework import serializers
from apps.governance.infrastructure.orm.models import Committee


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
