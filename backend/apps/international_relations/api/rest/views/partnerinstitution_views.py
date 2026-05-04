"""PartnerInstitution views."""
from rest_framework import viewsets, permissions
from apps.international_relations.infrastructure.orm.models import PartnerInstitution
from ..serializers.partnerinstitution_serializers import PartnerInstitutionSerializer


class PartnerInstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerInstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PartnerInstitution.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
