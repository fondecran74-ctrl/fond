"""GradeAppeal views."""
from rest_framework import viewsets, permissions
from apps.assessments.infrastructure.orm.models import GradeAppeal
from ..serializers.gradeappeal_serializers import GradeAppealSerializer


class GradeAppealViewSet(viewsets.ModelViewSet):
    serializer_class = GradeAppealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GradeAppeal.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
