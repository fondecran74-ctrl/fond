"""AuditLog views."""
from rest_framework import viewsets, permissions
from apps.audit_traceability.infrastructure.orm.models import AuditLog
from ..serializers.auditlog_serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AuditLog.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
