"""AI services models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class ChatSession(AuditableModel):
    """Chatbot conversation session."""
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="chat_sessions")
    title = models.CharField(max_length=200, blank=True, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "ai_chat_sessions"


class ChatMessage(AuditableModel):
    """Message in a chatbot session."""
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=20)
    content = models.TextField()
    metadata = models.JSONField(default=dict)

    class Meta:
        db_table = "ai_chat_messages"
        ordering = ["created_at"]


class Recommendation(AuditableModel):
    """AI-generated recommendation."""
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="recommendations")
    recommendation_type = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    description = models.TextField()
    confidence = models.DecimalField(max_digits=5, decimal_places=4)
    is_acted_upon = models.BooleanField(default=False)

    class Meta:
        db_table = "ai_recommendations"
