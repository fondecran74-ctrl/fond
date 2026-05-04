"""Graduation views."""
from rest_framework import viewsets, permissions
from apps.student_lifecycle.infrastructure.orm.models import Graduation
from ..serializers.graduation_serializers import GraduationSerializer


class GraduationViewSet(viewsets.ModelViewSet):
    serializer_class = GraduationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Graduation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
