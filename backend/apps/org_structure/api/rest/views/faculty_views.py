"""Faculty views."""
from rest_framework import viewsets, permissions
from apps.org_structure.infrastructure.orm.models import Faculty
from ..serializers.faculty_serializers import FacultySerializer


class FacultyViewSet(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Faculty.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
