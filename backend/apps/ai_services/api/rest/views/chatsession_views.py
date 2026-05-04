"""ChatSession views."""
from rest_framework import viewsets, permissions
from apps.ai_services.infrastructure.orm.models import ChatSession
from ..serializers.chatsession_serializers import ChatSessionSerializer


class ChatSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatSession.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
