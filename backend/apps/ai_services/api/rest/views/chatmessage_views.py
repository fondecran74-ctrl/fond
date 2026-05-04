"""ChatMessage views."""
from rest_framework import viewsets, permissions
from apps.ai_services.infrastructure.orm.models import ChatMessage
from ..serializers.chatmessage_serializers import ChatMessageSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatMessage.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
