"""AuditEntrySerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_audit import AuditEntry


class AuditEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditEntry
        fields = ["id", "actor", "action", "resource_type", "resource_id", "changes", "created_at"]
        read_only_fields = ["id", "created_at"]
