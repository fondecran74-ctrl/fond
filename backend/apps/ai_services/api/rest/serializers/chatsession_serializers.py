"""ChatSession serializer."""
from rest_framework import serializers
from apps.ai_services.infrastructure.orm.models import ChatSession


class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
