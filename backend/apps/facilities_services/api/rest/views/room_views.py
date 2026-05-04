"""Room views."""
from rest_framework import viewsets, permissions
from apps.facilities_services.infrastructure.orm.models import Room
from ..serializers.room_serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Room.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
