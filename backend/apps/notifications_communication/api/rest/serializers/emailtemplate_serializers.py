"""EmailTemplate serializer."""
from rest_framework import serializers
from apps.notifications_communication.infrastructure.orm.models import EmailTemplate


class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
