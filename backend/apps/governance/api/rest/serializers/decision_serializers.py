"""Decision serializer."""
from rest_framework import serializers
from apps.governance.infrastructure.orm.models import Decision


class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
