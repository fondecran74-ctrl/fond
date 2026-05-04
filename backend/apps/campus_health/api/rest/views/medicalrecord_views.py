"""MedicalRecord views."""
from rest_framework import viewsets, permissions
from apps.campus_health.infrastructure.orm.models import MedicalRecord
from ..serializers.medicalrecord_serializers import MedicalRecordSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicalRecord.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
