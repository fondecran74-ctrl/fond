"""Campus views."""
from rest_framework import viewsets, permissions
from apps.org_structure.infrastructure.orm.models import Campus
from ..serializers.campus_serializers import CampusSerializer


class CampusViewSet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Campus.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
