"""Semester views."""
from rest_framework import viewsets, permissions
from apps.academic_catalog.infrastructure.orm.models import Semester
from ..serializers.semester_serializers import SemesterSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    serializer_class = SemesterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Semester.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
