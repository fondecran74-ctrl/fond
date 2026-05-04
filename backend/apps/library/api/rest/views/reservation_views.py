"""Reservation views."""
from rest_framework import viewsets, permissions
from apps.library.infrastructure.orm.models import Reservation
from ..serializers.reservation_serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
