"""Announcement views."""
from rest_framework import viewsets, permissions
from apps.notifications_communication.infrastructure.orm.models import Announcement
from ..serializers.announcement_serializers import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Announcement.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
