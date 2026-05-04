"""PerformanceEvaluation views."""
from rest_framework import viewsets, permissions
from apps.hr.infrastructure.orm.models import PerformanceEvaluation
from ..serializers.performanceevaluation_serializers import PerformanceEvaluationSerializer


class PerformanceEvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = PerformanceEvaluationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PerformanceEvaluation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
