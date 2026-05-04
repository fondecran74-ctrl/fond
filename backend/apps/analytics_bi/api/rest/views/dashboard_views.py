"""Dashboard views."""
from rest_framework import viewsets, permissions
from apps.analytics_bi.infrastructure.orm.models import Dashboard
from ..serializers.dashboard_serializers import DashboardSerializer


class DashboardViewSet(viewsets.ModelViewSet):
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dashboard.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
