"""Audit Entry views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_audit import AuditEntry
from ..serializers.audit_serializers import AuditEntrySerializer


class AuditViewSet(viewsets.ModelViewSet):
    """Audit Entry management viewset."""
    serializer_class = AuditEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AuditEntry.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
