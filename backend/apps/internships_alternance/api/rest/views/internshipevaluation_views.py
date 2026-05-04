"""InternshipEvaluation views."""
from rest_framework import viewsets, permissions
from apps.internships_alternance.infrastructure.orm.models import InternshipEvaluation
from ..serializers.internshipevaluation_serializers import InternshipEvaluationSerializer


class InternshipEvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = InternshipEvaluationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InternshipEvaluation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
