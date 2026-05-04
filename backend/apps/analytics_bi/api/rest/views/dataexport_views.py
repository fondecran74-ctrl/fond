"""DataExport views."""
from rest_framework import viewsets, permissions
from apps.analytics_bi.infrastructure.orm.models import DataExport
from ..serializers.dataexport_serializers import DataExportSerializer


class DataExportViewSet(viewsets.ModelViewSet):
    serializer_class = DataExportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DataExport.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
