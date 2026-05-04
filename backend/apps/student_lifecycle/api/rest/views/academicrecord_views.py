"""AcademicRecord views."""
from rest_framework import viewsets, permissions
from apps.student_lifecycle.infrastructure.orm.models import AcademicRecord
from ..serializers.academicrecord_serializers import AcademicRecordSerializer


class AcademicRecordViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AcademicRecord.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
