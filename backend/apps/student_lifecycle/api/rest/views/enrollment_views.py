"""Enrollment views."""
from rest_framework import viewsets, permissions
from apps.student_lifecycle.infrastructure.orm.models import Enrollment
from ..serializers.enrollment_serializers import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
