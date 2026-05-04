"""ChatMessage serializer."""
from rest_framework import serializers
from apps.ai_services.infrastructure.orm.models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
