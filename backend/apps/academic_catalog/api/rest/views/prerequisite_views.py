"""Prerequisite views."""
from rest_framework import viewsets, permissions
from apps.academic_catalog.infrastructure.orm.models import Prerequisite
from ..serializers.prerequisite_serializers import PrerequisiteSerializer


class PrerequisiteViewSet(viewsets.ModelViewSet):
    serializer_class = PrerequisiteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prerequisite.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
