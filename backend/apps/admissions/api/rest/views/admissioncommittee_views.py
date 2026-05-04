"""AdmissionCommittee views."""
from rest_framework import viewsets, permissions
from apps.admissions.infrastructure.orm.models import AdmissionCommittee
from ..serializers.admissioncommittee_serializers import AdmissionCommitteeSerializer


class AdmissionCommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = AdmissionCommitteeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AdmissionCommittee.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
