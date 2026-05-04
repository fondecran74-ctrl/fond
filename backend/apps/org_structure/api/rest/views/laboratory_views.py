"""Laboratory views."""
from rest_framework import viewsets, permissions
from apps.org_structure.infrastructure.orm.models import Laboratory
from ..serializers.laboratory_serializers import LaboratorySerializer


class LaboratoryViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Laboratory.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
