"""LearningOutcome views."""
from rest_framework import viewsets, permissions
from apps.academic_catalog.infrastructure.orm.models import LearningOutcome
from ..serializers.learningoutcome_serializers import LearningOutcomeSerializer


class LearningOutcomeViewSet(viewsets.ModelViewSet):
    serializer_class = LearningOutcomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LearningOutcome.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
