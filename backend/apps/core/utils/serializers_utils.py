"""Serializer utility mixins."""
from rest_framework import serializers


class AuditFieldsMixin(serializers.Serializer):
    """Mixin providing audit fields."""
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
