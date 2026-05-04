"""ComplianceEvidence views."""
from rest_framework import viewsets, permissions
from apps.audit_traceability.infrastructure.orm.models import ComplianceEvidence
from ..serializers.complianceevidence_serializers import ComplianceEvidenceSerializer


class ComplianceEvidenceViewSet(viewsets.ModelViewSet):
    serializer_class = ComplianceEvidenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ComplianceEvidence.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
