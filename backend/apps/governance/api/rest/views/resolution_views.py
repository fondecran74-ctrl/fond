"""Resolution views."""
from rest_framework import viewsets, permissions
from apps.governance.infrastructure.orm.models import Resolution
from ..serializers.resolution_serializers import ResolutionSerializer


class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resolution.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
