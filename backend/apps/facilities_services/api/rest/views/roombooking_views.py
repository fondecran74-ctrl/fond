"""RoomBooking views."""
from rest_framework import viewsets, permissions
from apps.facilities_services.infrastructure.orm.models import RoomBooking
from ..serializers.roombooking_serializers import RoomBookingSerializer


class RoomBookingViewSet(viewsets.ModelViewSet):
    serializer_class = RoomBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RoomBooking.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
