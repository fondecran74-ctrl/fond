"""Incident views."""
from rest_framework import viewsets, permissions
from apps.itsm_cybersecurity.infrastructure.orm.models import Incident
from ..serializers.incident_serializers import IncidentSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
