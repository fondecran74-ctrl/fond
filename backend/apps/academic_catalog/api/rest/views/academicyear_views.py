"""AcademicYear views."""
from rest_framework import viewsets, permissions
from apps.academic_catalog.infrastructure.orm.models import AcademicYear
from ..serializers.academicyear_serializers import AcademicYearSerializer


class AcademicYearViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicYearSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AcademicYear.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
