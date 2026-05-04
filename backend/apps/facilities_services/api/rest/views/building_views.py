"""Building views."""
from rest_framework import viewsets, permissions
from apps.facilities_services.infrastructure.orm.models import Building
from ..serializers.building_serializers import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Building.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
