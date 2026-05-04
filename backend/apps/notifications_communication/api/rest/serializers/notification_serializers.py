"""Notification serializer."""
from rest_framework import serializers
from apps.notifications_communication.infrastructure.orm.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
