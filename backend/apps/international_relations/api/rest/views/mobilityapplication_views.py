"""MobilityApplication views."""
from rest_framework import viewsets, permissions
from apps.international_relations.infrastructure.orm.models import MobilityApplication
from ..serializers.mobilityapplication_serializers import MobilityApplicationSerializer


class MobilityApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = MobilityApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MobilityApplication.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
