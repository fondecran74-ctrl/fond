"""Accreditation views."""
from rest_framework import viewsets, permissions
from apps.quality_compliance_risk.infrastructure.orm.models import Accreditation
from ..serializers.accreditation_serializers import AccreditationSerializer


class AccreditationViewSet(viewsets.ModelViewSet):
    serializer_class = AccreditationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Accreditation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
