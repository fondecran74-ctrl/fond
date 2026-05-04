"""RiskRegister views."""
from rest_framework import viewsets, permissions
from apps.quality_compliance_risk.infrastructure.orm.models import RiskRegister
from ..serializers.riskregister_serializers import RiskRegisterSerializer


class RiskRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RiskRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RiskRegister.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
