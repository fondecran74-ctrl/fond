"""Grade views."""
from rest_framework import viewsets, permissions
from apps.assessments.infrastructure.orm.models import Grade
from ..serializers.grade_serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Grade.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
