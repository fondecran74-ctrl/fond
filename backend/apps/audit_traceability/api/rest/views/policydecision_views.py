"""PolicyDecision views."""
from rest_framework import viewsets, permissions
from apps.audit_traceability.infrastructure.orm.models import PolicyDecision
from ..serializers.policydecision_serializers import PolicyDecisionSerializer


class PolicyDecisionViewSet(viewsets.ModelViewSet):
    serializer_class = PolicyDecisionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PolicyDecision.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
