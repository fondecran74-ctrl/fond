"""Scholarship views."""
from rest_framework import viewsets, permissions
from apps.finance.infrastructure.orm.models import Scholarship
from ..serializers.scholarship_serializers import ScholarshipSerializer


class ScholarshipViewSet(viewsets.ModelViewSet):
    serializer_class = ScholarshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Scholarship.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
