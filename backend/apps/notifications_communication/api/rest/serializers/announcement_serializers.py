"""Announcement serializer."""
from rest_framework import serializers
from apps.notifications_communication.infrastructure.orm.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
