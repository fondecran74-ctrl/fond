"""Notification views."""
from rest_framework import viewsets, permissions
from apps.notifications_communication.infrastructure.orm.models import Notification
from ..serializers.notification_serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
