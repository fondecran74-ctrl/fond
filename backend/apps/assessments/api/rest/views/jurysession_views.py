"""JurySession views."""
from rest_framework import viewsets, permissions
from apps.assessments.infrastructure.orm.models import JurySession
from ..serializers.jurysession_serializers import JurySessionSerializer


class JurySessionViewSet(viewsets.ModelViewSet):
    serializer_class = JurySessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JurySession.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
