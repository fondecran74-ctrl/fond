"""Report views."""
from rest_framework import viewsets, permissions
from apps.analytics_bi.infrastructure.orm.models import Report
from ..serializers.report_serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
