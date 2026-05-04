"""QualityAudit views."""
from rest_framework import viewsets, permissions
from apps.quality_compliance_risk.infrastructure.orm.models import QualityAudit
from ..serializers.qualityaudit_serializers import QualityAuditSerializer


class QualityAuditViewSet(viewsets.ModelViewSet):
    serializer_class = QualityAuditSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return QualityAudit.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
