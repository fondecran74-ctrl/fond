"""Session views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_session import UserSession
from ..serializers.session_serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """Session management viewset."""
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserSession.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
