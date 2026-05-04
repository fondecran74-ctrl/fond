"""BreakGlassRequestSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_break_glass import BreakGlassRequest


class BreakGlassRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakGlassRequest
        fields = ["id", "requester", "approver", "status", "justification", "starts_at", "expires_at"]
        read_only_fields = ["id", "created_at"]
