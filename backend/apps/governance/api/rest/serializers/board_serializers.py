"""Board serializer."""
from rest_framework import serializers
from apps.governance.infrastructure.orm.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
