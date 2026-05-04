"""KPI views."""
from rest_framework import viewsets, permissions
from apps.quality_compliance_risk.infrastructure.orm.models import KPI
from ..serializers.kpi_serializers import KPISerializer


class KPIViewSet(viewsets.ModelViewSet):
    serializer_class = KPISerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return KPI.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
