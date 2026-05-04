"""Resolution serializer."""
from rest_framework import serializers
from apps.governance.infrastructure.orm.models import Resolution


class ResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resolution
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
