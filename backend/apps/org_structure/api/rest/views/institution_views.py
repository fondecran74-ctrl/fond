"""Institution views."""
from rest_framework import viewsets, permissions
from apps.org_structure.infrastructure.orm.models import Institution
from ..serializers.institution_serializers import InstitutionSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Institution.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
