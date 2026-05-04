"""Decision views."""
from rest_framework import viewsets, permissions
from apps.governance.infrastructure.orm.models import Decision
from ..serializers.decision_serializers import DecisionSerializer


class DecisionViewSet(viewsets.ModelViewSet):
    serializer_class = DecisionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Decision.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
