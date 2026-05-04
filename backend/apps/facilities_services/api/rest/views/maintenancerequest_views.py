"""MaintenanceRequest views."""
from rest_framework import viewsets, permissions
from apps.facilities_services.infrastructure.orm.models import MaintenanceRequest
from ..serializers.maintenancerequest_serializers import MaintenanceRequestSerializer


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MaintenanceRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
