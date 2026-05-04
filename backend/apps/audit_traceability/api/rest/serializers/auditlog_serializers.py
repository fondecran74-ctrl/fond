"""AuditLog serializer."""
from rest_framework import serializers
from apps.audit_traceability.infrastructure.orm.models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
