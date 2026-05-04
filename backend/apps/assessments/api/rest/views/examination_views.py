"""Examination views."""
from rest_framework import viewsets, permissions
from apps.assessments.infrastructure.orm.models import Examination
from ..serializers.examination_serializers import ExaminationSerializer


class ExaminationViewSet(viewsets.ModelViewSet):
    serializer_class = ExaminationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Examination.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
