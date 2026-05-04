"""Program views."""
from rest_framework import viewsets, permissions
from apps.academic_catalog.infrastructure.orm.models import Program
from ..serializers.program_serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Program.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
